import streamlit as st
import pickle
from responses import RESPONSES
from context_memory import save_context, get_context

# Load model
with open("intent_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("E-Commerce Assistant")

# Initialize chat history and context
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", "")


if user_input:
    intent = model.predict([user_input])[0]

    # Context keyword check
    keywords = ["Nike", "Adidas", "iPhone", "Samsung"]
    for kw in keywords:
        if kw.lower() in user_input.lower():
            save_context(kw)

    context = get_context()
    response = RESPONSES.get(intent, RESPONSES["Unknown/Other"])

    if context and intent == "Product Availability":
        response += f" (Previously mentioned: {context})"

    # Append to chat history
    st.session_state.chat_history.append((user_input, response))

# Display chat history
st.subheader("Chat History")
for user_msg, bot_msg in st.session_state.chat_history:
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**Agent:** {bot_msg}")