import streamlit as st
import imutils
import cv2
import numpy as np
import os
import requests
from controller import *

def app(box):
    st.title('AEmotional Intelligence')
    st.write('Real time video capture')

    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    global prediction
    prediction = "..."
    emotion = st.empty()
    run = st.button('run')

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
        if box:
            display(FRAME_WINDOW, color_canvas, faces_coordinates, rectangles=True, text=prediction)
        else:
            display(FRAME_WINDOW, color_canvas, faces_coordinates)
            emotion.empty()
            emotion.markdown(f"Emotional state: {prediction}")
    while run == False:
        ret, frame = camera.read()
        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
