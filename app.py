import streamlit as st
import imutils
import cv2
import numpy as np
import SessionState

'''
# Emotion Ai front
'''
# session_state = SessionState.get(api_image="", snap_btn=st.button('snapshot'))
FRAME_WINDOW = st.image([])
FRAME_WINDOW_2 = st.image([])
camera = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
box = st.checkbox('box')

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

def call_api(data):
    # body = {'X': cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)}
    # response = requests.post(url='/api/path-to-your-endpoint/', files=body)
    # st.write(print(response))
    pass

if st.button('Snapshot'):
    ret, frame = camera.read()
    gray_canvas =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_coordinates = get_faces_coordinates(gray_canvas)
    image = get_face_frames(gray_canvas, faces_coordinates)
    data = cv2.resize(image, dsize=(48, 48), interpolation=cv2.INTER_CUBIC)
    # emotion = call_api(data)
    st.write(data)

# while True:
#     ret, frame = camera.read()
#     color_canvas = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     gray_canvas =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces_coordinates = get_faces_coordinates(gray_canvas)
#     if box:
#         display(FRAME_WINDOW, color_canvas, faces_coordinates, rectangles=True)
#     else:
#         display(FRAME_WINDOW, color_canvas, faces_coordinates)



