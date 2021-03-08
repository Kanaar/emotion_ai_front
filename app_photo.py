import streamlit as st
from controller import *
import cv2
import numpy as np

def app(box):
    st.title('AEmotional Intelligence')
    st.write('Static image capture')
    FRAME_WINDOW = st.image([])

    emotion = st.empty()
    run = st.button('run')

    file = st.file_uploader('upload a file', type="jpg")
    if file is not None:
        file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        image = resize_import(image)
        color_canvas = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        gray_canvas = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces_coordinates = get_faces_coordinates(gray_canvas)
        render_frame(FRAME_WINDOW, color_canvas, faces_coordinates, "", emotion, box)

    if run and len(faces_coordinates) > 0:
        snapshot = take_snaphot(gray_canvas, faces_coordinates)
        response = call_api(snapshot)
        prediction = response['prediction']
        emotion.empty()
        emotion.markdown(f"Emotional state: {prediction}")
        render_frame(FRAME_WINDOW, color_canvas, faces_coordinates, prediction, emotion, box)


