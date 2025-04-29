
import streamlit as st

def save_context(keyword):
    st.session_state["context"] = keyword

def get_context():
    return st.session_state.get("context", None)
