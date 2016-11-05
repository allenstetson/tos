import os
import sys
import json
import pytz
import time
import urllib2
import datetime
from flask import Flask, render_template, Markup
sys.path.insert(0, '.')
import wetaVisitData
import notification

import pdb

app = Flask(__name__)

TIMEOUT = 30 # Currently unused, global setting for timeout (html redirect)
PANE_LOCATION = "./static/panes/"

#---------------------------
# main
# Main entry point for TOS webPortal traffic
#---------------------------
@app.route('/')
def main():
    # Get weather:
    nzWeatherInfo = WeatherInfo('Wellington,nz').getInfoFromAPI()
    laWeatherInfo = WeatherInfo('Manhattan_Beach,us').getInfoFromAPI()
    # Get data for summary sidebar
    summary = Markup("\n".join(getHourlySummary()))
    # Get Panes for Main Window
    panes = Markup("\n".join(getPanes()))
    return render_template('main.htm', nzWeatherInfo=nzWeatherInfo,
                           laWeatherInfo=laWeatherInfo, panes=panes, summaryContent=summary)

def getPanes():
    allPanes = []
    for content in os.listdir(PANE_LOCATION):
        if not os.path.isfile(PANE_LOCATION+content):
            continue
        fh = open(PANE_LOCATION+content)
        url = fh.readline().strip()
        fh.close()
        #sanitize:
        if url.startswith("\""):
            url = url[1:]
        if url.endswith("\""):
            url = url[:-1]
        allPanes.append('<p class="windowPane"><iframe src="%s" style="border:0px;" ' % url +
                        'width="100%" height="100%"></iframe></p>')
    return allPanes

def getHourlySummary():
    activeEvents = []
    imminentEvents = []
    nextEvents = []
    data = wetaVisitData.getVisitData()
    today = datetime.date.today().strftime("%m/%d/%Y")
    now = datetime.datetime.now()
    if not data.has_key(today):
        print("WARNING: No entries for today")
        return ""
    events = data[today]
    for event in events:
        startTime = datetime.datetime.strptime("%s %s" % (today, event['startTime']), "%m/%d/%Y %H:%M")
        endTime = datetime.datetime.strptime("%s %s" % (today, event['endTime']), "%m/%d/%Y %H:%M")
        delta = startTime-now
        if now > startTime:
            #We may need to be in this meeting. Check End for a delta less than, oh, 6 hours.
            if now < endTime:
                print("Found active event: %s" % event['title'])
                activeEvents.append(event)
        elif delta.seconds/60 < 30:
            #Coming up within thirty mins!
            print("Found imminent event: %s" % event['title'])
            imminentEvents.append(event)
        elif delta.seconds/60/60 < 2:
            # Coming up within the next 2 hours
            print("Found upcoming event: %s" % event['title'])
            nextEvents.append(event)
        else:
            continue
    formattedSummary = formatSummary(activeEvents, imminentEvents, nextEvents)
    return formattedSummary

def formatSummary(activeEvents, imminentEvents, nextEvents):
    output = []
    for event in activeEvents:
        output.append('<p class="summaryTitle">%s - %s</p>' % (event['startTime'], event['endTime']))
        output.append('<div class="summarySection">%s</div>' % event['title'])
        output.append('<div class="summarySubsection">%s</div>' % event['location'])
        output.append('<div class="summaryBody">%s</div>' % ", ".join(event['attendees']))
    for event in imminentEvents:
        output.append('<p class="summaryNextTitle">%s - %s</p>' % (event['startTime'], event['endTime']))
        output.append('<div class="summaryNextSection">%s</div>' % event['title'])
        output.append('<div class="summaryNextSubsection">%s</div>' % event['location'])
        output.append('<div class="summaryNextBody">%s</div>' % ", ".join(event['attendees']))
    for event in nextEvents:
        output.append('<p class="summaryNextTitle">%s - %s</p>' % (event['startTime'], event['endTime']))
        output.append('<div class="summaryNextSection">%s</div>' % event['title'])
        output.append('<div class="summaryNextSubsection">%s</div>' % event['location'])
        output.append('<div class="summaryNextBody">%s</div>' % ", ".join(event['attendees']))
    return output

#---------------------------
# tosClock
# A timezone/daylight savings aware clock that shows time in NZ and LA, and weather
#---------------------------
@app.route('/tosClock')
def tosClock():
    date = datetime.datetime.now()
    #Get weather:
    nzWeatherInfo = WeatherInfo('Wellington,nz').getInfoFromAPI()
    laWeatherInfo = WeatherInfo('Manhattan_Beach,us').getInfoFromAPI()
    return render_template('TOSClock.htm', date=date, nzWeatherInfo=nzWeatherInfo,
                           laWeatherInfo=laWeatherInfo, timeout=TIMEOUT)

class WeatherInfo(dict):
    def __init__(self, place):
        super(WeatherInfo, self).__init__()
        weatherApiKey = "7ef3ef345316959c479dda977fa1f87c"
        weatherApiURL = "http://api.openweathermap.org/data/2.5/weather?q="
        self['weatherURL'] = "%s%s&appid=%s" % (weatherApiURL, place, weatherApiKey)
        self['weatherDataDir'] = "/tmp"
        self['weatherDataFile'] = "%s/weatherData_%s.json" % (self['weatherDataDir'], place)

    def getInfoFromAPI(self):
        data = self._getRecentCache()
        if not data:
            print("Opening URL: %s" % self['weatherURL'])
            response = urllib2.urlopen(self['weatherURL'])
            data = json.load(response)
            if not os.path.exists(self['weatherDataDir']):
                os.makedirs(self['weatherDataDir'])
            fh = open(self['weatherDataFile'], 'w')
            json.dump(data, fh)
            fh.close()
        self._fillThings(data)
        return(self)

    def _getRecentCache(self):
        if not os.path.exists(self['weatherDataFile']):
            return False
        st = os.stat(self['weatherDataFile'])
        mtime = st.st_mtime
        timeNow = time.time()
        age = int((timeNow - mtime) / 60)
        if age > 30:
            return False
        fh = open(self['weatherDataFile'], 'r')
        data = json.loads(fh.read())
        fh.close()
        return data

    def _fillThings(self, info):
        self['iconURL'] = "http://openweathermap.org/img/w/%s.png" % (info['weather'][0]['icon'])
        self['description'] = info['weather'][0]['description'].title()
        self['temp_c'] = round(info['main']['temp'] - 273.15)
        self['temp_f'] = round(info['main']['temp'] * (9.0/5.0) - 459.67)
        self['windspeed_k'] = round(info['wind']['speed'] * 1.94384449, 2)

@app.route('/clockUpdate')
def clockUpdate():
    valueNz = datetime.datetime.now(pytz.timezone('Pacific/Auckland'))
    valueLa = datetime.datetime.now(pytz.timezone('US/Pacific'))
    printNzTime = "%02d:%02d:%02d" % (valueNz.hour, valueNz.minute, valueNz.second)
    printLaTime = "%02d:%02d:%02d" % (valueLa.hour, valueLa.minute, valueLa.second)
    printNzDate = "%s %02d/%02d/%d" % (valueNz.strftime("%a"), valueNz.month, valueNz.day, valueNz.year)
    printLaDate = "%s %02d/%02d/%d" % (valueLa.strftime("%a"), valueLa.month, valueLa.day, valueLa.year)
    return json.dumps(
        {'nzTime':printNzTime,
         'laTime':printLaTime,
         'nzDate':printNzDate,
         'laDate':printLaDate
         })

#---------------------------
# summaryUpdate
# Function that updates the summary window
#---------------------------
@app.route('/summaryUpdate')
def summaryUpdate():
    return Markup("\n".join(getHourlySummary()))

#---------------------------
# notificationCheck
# Function that checks for any alerts
#---------------------------
@app.route('/notificationCheck')
def notificationCheck():
    emailNotificationChecker = notification.IncomingEmailNotification()
    alerts = emailNotificationChecker.checkForNotifications()
    if alerts:
        return json.dumps((True, alerts))
    else:
        return json.dumps((False, []))

#---------------------------
# *** CURRENTLY UNUSED ***
# calAllen
# A page that shows Allen's calendar and daily status / availability
#---------------------------
@app.route('/calAllen')
def calAllen():
    attendance = "In the Office"
    if attendance == "In the Office":
        attendanceColor = "#00AA00"
    elif attendance == "Out of the Office":
        attendanceColor = "#990000"
    elif attendance == "Temporarily Unavailable":
        attendanceColor = "#0033CC"
    else:
        attendanceColor = "#999999"
    return render_template('calAllen.htm', attendance=attendance, attendanceColor=attendanceColor, timeout=TIMEOUT)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)




my_date = datetime.datetime.now()
