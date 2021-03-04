import streamlit as st
import imutils
import cv2
import numpy as np

'''
# Emotion Ai front
'''

FRAME_WINDOW = st.image([])
FRAME_WINDOW_2 = st.image([])
camera = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
snap_btn = st.button('snapshot')
# while True:
#     ret, frame = camera.read()
#     color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     FRAME_WINDOW.image(color)

if snap_btn:
    st.write('SNAP!')
    ret, frame_2 = camera.read()
    gray = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)
    FRAME_WINDOW_2.image(gray)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(48, 48),
    )
    for (x, y, w, h) in faces:
        rect_image = cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
        FRAME_WINDOW_2.image(rect_image)


    # body = {'X': cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)}
    # response = requests.post(url='/api/path-to-your-endpoint/', files=body)
    # st.write(print(response))
