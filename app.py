import streamlit as st
from pages.Home import show as home
from pages.Dashboard import show as dashboard
from pages.Paste import show as paste
from pages.Download import show as download

# Set page config as the first Streamlit command
st.set_page_config(page_title="YouTube Sentiment Tracker", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Dashboard", "Paste", "Download"])

# Route to each page
if page == "Home":
    home()
elif page == "Dashboard":
    dashboard()
elif page == "Paste":
    paste()
elif page == "Download":
    download()

