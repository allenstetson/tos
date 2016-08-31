from gevent import monkey; monkey.patch_all()
from ws4py.websocket import EchoWebSocket
from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication
import flask

from flask import Flask, render_template, request
app = Flask(__name__)
server = WSGIServer(('localhost', 9000), WebSocketWSGIApplication(handler_cls=EchoWebSocket))
server.serve_forever()

@app.route('/')
def main():
    return render_template('main.htm')
