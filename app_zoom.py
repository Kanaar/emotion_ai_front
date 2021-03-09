import streamlit as st
import streamlit.components.v1 as components

def app(box):
    HtmlFile = open("zoom_component.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code)
