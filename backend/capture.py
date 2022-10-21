import cv2
import mediapipe as mp
import time

from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import image as im
import pickle
import argparse
import pygame

# Mediapipe API
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

pygame.init()

RECORD_TIME = 10

parser = argparse.ArgumentParser()
parser.add_argument("--gesture", help="Gesture to be recorded", type=str, default=None)
parser.add_argument("--knn", help="Filename of pickled KNN", type=str, default=None)
parser.add_argument("--data_dir", help="Directory to save data to", type=str, default="data")
args = parser.parse_args()

if args.knn:
  knn_file = open(args.knn, 'rb')     
  knn = pickle.load(knn_file)

start = time.time()
header = ""
world_landmarks = []
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity = 0,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
    ) as hands:

  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

  # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
      for hand_world_landmarks in results.multi_hand_world_landmarks:
        world_landmarks.append(hand_world_landmarks)
        if args.knn:
          landmarks = hand_world_landmarks.landmark
          data_point = []
          for point in landmarks:
            data_point += [point.x, point.y, point.z, point.visibility]
          header = str(knn.predict([data_point])[0])


      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    # Flip the image horizontally for a selfie-view display.
    image = cv2.flip(image, 1)
    cv2.putText(image, header, (50,350), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1.5, color = (57, 255, 20), thickness=5)
    cv2.imshow('MediaPipe Hands', image)
    header = ""

    #When you click escape, then the window closes
    for event in pygame.event.get():
      pass
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      im1 = Image.fromarray(image)
      im1 = im1.save("hands.jpg")
      break
    

    if args.gesture:
      print(time.time() - start)
      if time.time() - start > RECORD_TIME:
        with open("{}/{}".format(args.data_dir, args.gesture), "wb+") as fp:
          pickle.dump(world_landmarks, fp)
          break
        
      
 
cap.release()
