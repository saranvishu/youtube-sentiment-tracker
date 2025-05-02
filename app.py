from pages.Home import show as home
from pages.Dashboard import show as dashboard
from pages.Paste import show as paste
from pages.Download import show as download
from pages.Emotion import show as emotion
import streamlit as st

st.set_page_config(page_title="YouTube Sentiment Tracker", layout="wide")

st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Go to", ["Home", "Paste Comments", "Dashboard", "Emotion Analysis", "Download Data"])

if app_mode == "Home":
    from pages.Home import show as home
    home()

elif app_mode == "Paste Comments":
    from pages.Paste import show as paste
    paste()

elif app_mode == "Dashboard":
    from pages.Dashboard import show as dashboard
    dashboard()

elif app_mode == "Emotion Analysis":
    from pages.Emotion import show as emotion
    emotion()

elif app_mode == "Download Data":
    from pages.Download import show as download
    download()
