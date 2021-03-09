RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
web: sh setup.sh && streamlit run app.py
