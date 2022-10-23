import cv2
import mediapipe as mp
from PIL import Image
import pickle
import argparse
import serial
import time
import random


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
correct = True
practice_letter, chain = '', ''

write = False

camera = cv2.VideoCapture(0)
start = time.time()
score = 0

def set_write(write_val):
    global write, start, score, chain
    write = write_val
    start = time.time()
    score = 0
    chain = ''

def gen_frames():  
    global correct, practice_letter, score, chain
    start = time.time()
    letter, cur_letter, last_letter = '', '', ''
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
                    count = count + 1 if (cur_letter == letter and (last_letter != letter or not write)) else 0
                    cur_letter = letter
                    if count > 5 and letter != "thumbs_down":
                        count = 0
                        if letter != "open": 
                            if practice_letter == letter:
                                correct = True
                                score += 1
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
            if write:
                cv2.putText(image, chain, (50,450), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1.5, color = (255, 57, 20), thickness=5)     
            else:
                cv2.putText(image, "Time elapsed: {} Score: {}".format(str(round(time.time() - start, 2)), score), 
                        (50,600), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1.5, color = (57, 255, 20), thickness=5)    

            ret, buffer = cv2.imencode('.jpg', image)
            image = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')


def get_images(type="signs"):
    global correct, practice_letter, score
    while True:
        letters = ['A']#,'B','C','D', 'E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
        if correct:
            practice_letter = random.choice(letters)
            correct = False
        image = cv2.imread('/Users/liampilarski/Desktop/ASL_HackGT9/frontend/build/{}/{}.jpg'.format(type, practice_letter))
        ret, buffer = cv2.imencode('.jpg', image)
        image = buffer.tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')