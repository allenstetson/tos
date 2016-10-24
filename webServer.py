'''
Allen this doesn't work as is. IT hangs indefinitely without reporting a port for te socket.
'''

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WetaTOS#FTW!'
socketio = SocketIO(app)

response = [{'name':'scooby', 'last':'doo', 'where':'rU'}]

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(json.dumps(response), broadcast=True)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    send(json.dumps(response))

@socketio.on('my event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@app.route('/')
def main():
    return render_template('main.htm')

if __name__ == '__main__':
    socketio.run(app)