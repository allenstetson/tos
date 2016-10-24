'''
The ws connect works to serve flask info.
server for websocket does not work.
'''

from gevent import monkey
monkey.patch_all()

import cgi
from ws4py.websocket import EchoWebSocket
from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication
from ws4py.client.geventclient import WebSocketClient

from flask import Flask, render_template, request

app = Flask(__name__)
ws = WebSocketClient('ws://localhost:9000/echo', protocols=['http-only', 'chat'])

def incoming():
    while True:
        m = ws.receive()
        if m is not None:
            print(str(m))
        else:
            break


@app.route('/')
def main():
    return render_template('main.htm')


if __name__ == '__main__':
#    server = WSGIServer(('localhost', 9000), WebSocketWSGIApplication(handler_cls=EchoWebSocket))
#    server.start()
    #print(dir(server))
    app.run(debug=True)
    ws.connect()
