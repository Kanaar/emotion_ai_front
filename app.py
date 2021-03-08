import streamlit as st
import imutils
import cv2
import numpy as np
import os
import requests

'''
# Emotion Ai front
'''
FRAME_WINDOW = st.image([])
FRAME_WINDOW_2 = st.image([])
camera = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
global prediction
prediction = "..."
box = st.sidebar.checkbox("box faces")
emotion = st.sidebar.empty()
run = st.sidebar.button('run')

def get_faces_coordinates(canvas):
    return faceCascade.detectMultiScale(
        canvas,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(55, 55)
    )

def get_face_frames(canvas, faces_coordinates):
    for (x, y, w, h) in faces_coordinates:
        return canvas[y:y + h, x:x + w]

def display(window, canvas, faces_coordinates, rectangles=False, text=""):
    if rectangles:
        for (x, y, w, h) in faces_coordinates:
            canvas = cv2.rectangle(canvas, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(canvas, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        window.image(canvas)
    else:
        window.image(canvas)

def call_api(snapshot):
    np.save('snapshot', snapshot)
    url='http://127.0.0.1:8000/predict_array'
    files = {'files': open('snapshot.npy', 'rb')}
    response = requests.post(url, files=files)
    os.remove('snapshot.npy')
    return response.json()

def take_snaphot(canvas, faces_coordinates):
    image = get_face_frames(canvas, faces_coordinates)
    snapshot = cv2.resize(image, dsize=(48, 48), interpolation=cv2.INTER_CUBIC)
    return snapshot

count = 0
while run:
    count += 1
    ret, frame = camera.read()
    color_canvas = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray_canvas =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_coordinates = get_faces_coordinates(gray_canvas)
    if count > 20 and len(faces_coordinates) > 0:
        count = 0
        snapshot = take_snaphot(gray_canvas, faces_coordinates)
        response = call_api(snapshot)
        prediction = response['prediction']
        emotion.empty()
        emotion.markdown(f"Emotional state: {prediction}")
    if box:
        display(FRAME_WINDOW, color_canvas, faces_coordinates, rectangles=True, text=prediction)
    else:
        display(FRAME_WINDOW, color_canvas, faces_coordinates)




