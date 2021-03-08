import app_photo
import app_video
import streamlit as st

print("App launching...")
PAGES = {"Video": app_video, "Photo": app_photo}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
box = st.sidebar.checkbox("box faces")

page = PAGES[selection]
page.app(box)
