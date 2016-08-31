from ws4py.client.threadedclient import WebSocketClient
import notification
import json

class NotificationClient(WebSocketClient):
    def getNotificationStatus(self):
        emailNotif = notification.IncomingEmailNotification()
        status = emailNotif.checkForNotifications()
        return(json.dumps(status))

    def opened(self):
        print("Opened websocket connection.")
        self.send(self.getNotificationStatus())

    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    def received_message(self, m):
        print(m)
        if len(m) == 175:
            self.close(reason='Bye bye')

if __name__ == '__main__':
    try:
        ws = NotificationClient('ws://localhost:9000/', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()