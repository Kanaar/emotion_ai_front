import streamlit as st
from controller import *
import cv2
import numpy as np

def app(box):
    st.title('AEmotional Intelligence')
    st.write('Static image capture')

    global prediction
    prediction = "..."
    emotion = st.empty()
    run = st.button('run')

    file = st.file_uploader('upload a file', type="jpg")
    if file is not None:
        file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        st.image(opencv_image, channels="BGR")
        gray_canvas = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces_coordinates = get_faces_coordinates(gray_canvas)

    if run and len(faces_coordinates) > 0:
        snapshot = take_snaphot(gray_canvas, faces_coordinates)
        response = call_api(snapshot)
        prediction = response['prediction']
        emotion.empty()
        emotion.markdown(f"Emotional state: {prediction}")

    # if box:
    #     display(FRAME_WINDOW, color_canvas, faces_coordinates, rectangles=True, text=prediction)
    # else:
    #     display(FRAME_WINDOW, color_canvas, faces_coordinates)

