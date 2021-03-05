import streamlit as st
import imutils
import cv2
import numpy as np
import SessionState
import os
import requests

'''
# Emotion Ai front
'''
# session_state = SessionState.get(api_image="", snap_btn=st.button('snapshot'))
FRAME_WINDOW = st.image([])
FRAME_WINDOW_2 = st.image([])
camera = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
box = st.checkbox('box')
global snapshot_btn
snapshot_btn = st.button('Snapshot')
# session_state = SessionState(user_name='', favorite_color='black')

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

def display(window, canvas, faces_coordinates, rectangles=False):
    if rectangles:
        for (x, y, w, h) in faces_coordinates:
            display_canvas = cv2.rectangle(canvas, (x, y), (x+w, y+h), (0, 255, 0), 2)
        window.image(display_canvas)
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

while True:
    ret, frame = camera.read()
    color_canvas = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray_canvas =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_coordinates = get_faces_coordinates(gray_canvas)
    if box:
        display(FRAME_WINDOW, color_canvas, faces_coordinates, rectangles=True)
    else:
        display(FRAME_WINDOW, color_canvas, faces_coordinates)
    if snapshot_btn:
        snapshot_btn = False
        snapshot = take_snaphot(gray_canvas, faces_coordinates)
        response = call_api(snapshot)
        st.write(response['prediction'])


