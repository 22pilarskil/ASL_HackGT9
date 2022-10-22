#Import necessary libraries
from flask import Flask, render_template, Response, request, jsonify, send_from_directory
from flask_socketio import SocketIO,emit
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import frames
import time

from HelloApiHandler import HelloApiHandler

#Initialize the Flask app
app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)
api = Api(app)

api.add_resource(HelloApiHandler, '/flask/hello')

@app.route('/')
def index():
    return send_from_directory(app.static_folder,'index.html')
    # return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(frames.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)