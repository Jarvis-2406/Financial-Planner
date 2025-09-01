import streamlit as st

st.set_page_config(page_title="Financial Planner", page_icon="💰", layout="wide")

try:
    with open("Financial Tracker.html", "r", encoding="utf-8") as f:
        html = f.read()
    # Render your HTML inside Streamlit
    st.components.v1.html(html, height=900, scrolling=True)
except FileNotFoundError:
    st.error("`Financial Tracker.html` not found in the repo root.")
