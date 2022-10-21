#Import necessary libraries
from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
from PIL import Image
import pickle
import argparse
import serial
import time


# User defined constants
WIDTH, HEIGHT = 640, 480
RECORD_TIME = 10

# Required variables

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

knn_file = open('asl_knn', 'rb')     
knn = pickle.load(knn_file)

hands = mp_hands.Hands(
    model_complexity = 0,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5,
    max_num_hands = 1
    )



#Initialize the Flask app
app = Flask(__name__)

camera = cv2.VideoCapture(0)

def gen_frames():  

    start = time.time()
    letter, cur_letter, last_letter, chain = "", "", "", ""
    count = 0

    while True:
        success, image = camera.read()  # read the camera frame
        if not success:
            break
        else:

            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_world_landmarks in results.multi_hand_world_landmarks:
                    landmarks = hand_world_landmarks.landmark
                    data_point = []
                    for point in landmarks:
                        data_point += [point.x, point.y, point.z, point.visibility]
                    letter = str(knn.predict([data_point])[0])
                    count = count + 1 if (cur_letter == letter and last_letter != letter) else 0
                    cur_letter = letter
                    if count > 5 and letter != "thumbs_down":
                        count = 0
                        if letter != "open": 
                            chain += letter
                            last_letter = letter
                        else: last_letter = ""
                    if count > 20 and letter == "thumbs_down":
                        count = 0
                        try: 
                            chain = chain[:-1]
                        except:
                            pass
                    

                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())  
                        
            image = cv2.flip(image, 1)
            cv2.putText(image, letter, (50,350), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1.5, color = (57, 255, 20), thickness=5)     
            cv2.putText(image, chain, (50,450), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1.5, color = (255, 57, 20), thickness=5)     

            ret, buffer = cv2.imencode('.jpg', image)
            image = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)