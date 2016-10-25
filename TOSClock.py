import os
import json
import pytz
import time
import urllib2
import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

TIMEOUT = 30

@app.route('/')
def main():
    date = datetime.datetime.now()
    #Get weather:
    nzWeatherInfo = WeatherInfo('Wellington,nz').getInfoFromAPI()
    laWeatherInfo = WeatherInfo('Manhattan_Beach,us').getInfoFromAPI()
    return render_template('TOSClock.htm', date=date, nzWeatherInfo=nzWeatherInfo, laWeatherInfo=laWeatherInfo, timeout=TIMEOUT)

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
    printNzDate = "%02d/%02d/%d" % (valueNz.month, valueNz.day, valueNz.year)
    printLaDate = "%02d/%02d/%d" % (valueLa.month, valueLa.day, valueLa.year)
    return json.dumps(
        {'nzTime':printNzTime,
         'laTime':printLaTime,
         'nzDate':printNzDate,
         'laDate':printLaDate
         })

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
