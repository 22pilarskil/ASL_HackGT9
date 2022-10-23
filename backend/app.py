#Import necessary libraries
from flask import Flask, Response, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import frames
import time

class RequestHandler(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('write', type=int)
    args = parser.parse_args()
    frames.set_write(args.write)


#Initialize the Flask app
app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)
api = Api(app)

api.add_resource(RequestHandler, '/flask/hello')

@app.route('/')
def index():
    return send_from_directory(app.static_folder,'index.html')
    # return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(frames.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/image_feed')
def image_feed():
    return Response(frames.get_images(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_time')
def get_time():
    return Response(time.time() - frames.start, mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True)