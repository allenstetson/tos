'''
This sort of works. It serves indefinitely without reporting a port, but accessing 9000 does generate
a handshake error. 9000 seems to be accessible.
'''

from gevent import monkey; monkey.patch_all()
from ws4py.websocket import EchoWebSocket
from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication

server = WSGIServer(('localhost', 9000), WebSocketWSGIApplication(handler_cls=EchoWebSocket))
server.serve_forever()