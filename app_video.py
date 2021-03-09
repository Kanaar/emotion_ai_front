import streamlit as st
import cv2
from controller import *
from streamlit_webrtc import webrtc_streamer


webrtc_streamer(key="example")

def app(box):
    st.title('AEmotional Intelligence')
    st.write('Real time video capture')

    camera = None#cv2.VideoCapture(0)
    FRAME_WINDOW = st.image([])
    global prediction
    prediction = "..."

    emotion = st.empty()
    run = st.button('run')

    count = 0
    if False:#while True:
        count += 1
        ret, frame = camera.read()
        color_canvas = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray_canvas =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_coordinates = get_faces_coordinates(gray_canvas)
        if run:
            if count > 20 and len(faces_coordinates) > 0:
                count = 0
                snapshot = take_snaphot(gray_canvas, faces_coordinates)
                response = call_api(snapshot)
                prediction = response['prediction']
        render_frame(FRAME_WINDOW, color_canvas, faces_coordinates, prediction, emotion, box)

