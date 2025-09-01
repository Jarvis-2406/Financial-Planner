import streamlit as st

st.set_page_config(page_title="Financial Planner", page_icon="💰", layout="wide")

st.sidebar.title("💼 Financial Planner")
st.sidebar.markdown(
    """
    - Edit `index.html` to change the UI  
    - Push to GitHub → auto-redeploy
    """
)

try:
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    # Render your HTML inside Streamlit
    st.components.v1.html(html, height=900, scrolling=True)
except FileNotFoundError:
    st.error("`index.html` not found in the repo root.")
