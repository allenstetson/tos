import os
import json
import poplib
from observer import Observable

'''
from Observer import Observer, Observable

class Flower:
    def __init__(self):
        self.isOpen = 0
        self.openNotifier = Flower.OpenNotifier(self)
        self.closeNotifier= Flower.CloseNotifier(self)
    def open(self): # Opens its petals
        self.isOpen = 1
        self.openNotifier.notifyObservers()
        self.closeNotifier.open()
    def close(self): # Closes its petals
        self.isOpen = 0
        self.closeNotifier.notifyObservers()
        self.openNotifier.close()
    def closing(self): return self.closeNotifier

    class OpenNotifier(Observable):
        def __init__(self, outer):
            Observable.__init__(self)
            self.outer = outer
            self.alreadyOpen = 0
        def notifyObservers(self):
            if self.outer.isOpen and \
            not self.alreadyOpen:
                self.setChanged()
                Observable.notifyObservers(self)
                self.alreadyOpen = 1
        def close(self):
            self.alreadyOpen = 0
'''

class IncomingEmailNotification(object):
    def __init__(self):
        self.hasNewAlert = False
        self.notifierNewAlert = IncomingEmailNotification.NotifierNewAlert(self)

    class NotifierNewAlert(Observable):
        def __init__(self, outer):
            Observable.__init__(self)
            self.outer = outer
            self.alertAlreadySent = False
        def notifyObservers(self):
            if self.outer.hasNewAlert and self.alertAlreadySent:
                self.setChanged()
                Observable.notifyObservers(self)
                self.alertAlreadySent = True
        def close(self):
            self.alertAlreadySent = False

    def _checkForNewMail(self, mailbox):
        lastReadInboxLocation = '%s/.tosEmailInbox.json' % os.environ['HOME']
        # Load last-read inbox
        with open(lastReadInboxLocation, 'r') as fh:
            oldInbox = json.loads(fh.read())
        # Load new inbox
        newInbox = mailbox.list()[1]
        newEmail = []
        # Compare inboxes
        if not oldInbox == newInbox:
            # Something has changed.  Is it new mail?
            newEmail = list(set(newInbox) - set(oldInbox))
        # Update last-read inbox
#        with open(lastReadInboxLocation, 'w') as fh:
#            fh.write(json.dumps(newInbox))

        if newEmail:
            return(newEmail)

    def _checkNewMsgForImportance(self, msg):
        subject = ""
        for line in msg:
            if line.startswith('Subject:'):
                subject = line.split()
                if subject[1] == "[TOS":
                    return True

    def checkForNotifications(self):
        notificationsRaw = []
        with MailConnection() as mailbox:
            newEmail = self._checkForNewMail(mailbox)
            if not newEmail:
                return False
            for mailString in newEmail:
                index = mailString.split()[0]
                msg = mailbox.retr(index)[1]
                isImportant = self._checkNewMsgForImportance(msg)
                if isImportant:
                    notificationsRaw.append(msg)
        if notificationsRaw:
            self.hasNewAlert = True
            self.notifierNewAlert.notifyObservers()

        return list(map(lambda x: TOSNotification(x), notificationsRaw))


class MailConnection(object):
    def __init__(self):
        self.mailbox = self._connectToMailbox()

    def __enter__(self):
        return self.mailbox

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mailbox.quit()

    def _connectToMailbox(self):
        mailbox = poplib.POP3_SSL('pop.jisunandallen.com', '995')
        user = 'allen@jisunandallen.com'
        pass_ = '5Nnrnh5!'
        mailbox.user(user)
        mailbox.pass_(pass_)
        return(mailbox)


class TOSNotification(dict):
    def __init__(self, msg):
        super(TOSNotification, self).__init__()
        self['type'] = None
        self['sender'] = None
        self['subject'] = None
        self['user'] = None
        self['host'] = None
        self['location'] = None
        self['received'] = None
        self._populate(msg)

    def _populate(self, msg):
        beginBody = False
        body = []
        for line in msg:
            if beginBody == True:
                if line.startswith("Content-Type"):
                    beginBody = "Finished"
                else:
                    if line.startswith("location:"):
                        self['location'] = line.split()[1]
                    elif line.startswith("user:"):
                        self['user'] = line.split()[1]
                    elif line.startswith("host:"):
                        self['host'] = line.split()[1]
                    body.append(line)
            # Subject & Type
            if line.startswith("Subject:"):
                self['subject'] = " ".join(line.split()[1:])
                if line.split()[1] == "[TOS":
                    myType= line.split()[2].lower()[:-1]
                    if myType in ['alert','note','calendar','out','late']:
                        self['type'] = myType
            elif line.startswith("From:"):
                self['sender'] = " ".join(line.split()[1:])
            elif line.startswith("Content-Type: text") and beginBody == False:
                beginBody = True
            elif line.startswith("Received: by") and ";" in line:
                self['received'] = line.split(";")[1].strip()
        self['body'] = "\n".join(body)

