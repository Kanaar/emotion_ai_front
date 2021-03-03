import streamlit as st
import cv2

'''
# Emotion Ai front
'''

st.markdown(''' do cool stuff ''')

run = st.checkbox('activate')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')

'''

1.a button to take a snapshot
1.b take a snapshot at interval

2.a convert snapshot to grayscale
2.b crop the snapshot to 48*48

3. call the api with requests
'''

url = 'http://taxifare.lewagon.ai/predict_fare/'

if url == 'http://taxifare.lewagon.ai/predict_fare/':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

NEXT: React on the api responses. i.e. interact with the user

'''
