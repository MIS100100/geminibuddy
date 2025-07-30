import streamlit as st
import google.generativeai as genai

# Gemini API key set karo (apni API key yahan lagao)
genai.configure(api_key="AIzaSyBTT6RXwH-lKWwuCF4ybxwEXUrc6T6uJW0")

model = genai.GenerativeModel('gemini-pro')

# Chat history maintain karne ke liye
if "conversation" not in st.session_state:
    st.session_state.conversation = []

st.title("🌟 GeminiBuddy: Tumhara AI Dost")

st.write("Namaste! Main GeminiBuddy hoon, tumhari madad ke liye yahan hoon. Kya padhna chahte ho ya koi sawaal hai?")

def get_bot_response(user_message):
    st.session_state.conversation.append({"role": "user", "content": user_message})

    response = model.generate_message(
        messages=st.session_state.conversation,
        temperature=0.7,
    )

    bot_message = response.last.message["content"]
    st.session_state.conversation.append({"role": "assistant", "content": bot_message})
    return bot_message

user_input = st.text_input("Tum kya puchna chahte ho?", key="input")

if user_input:
    bot_reply = get_bot_response(user_input)
    st.write(f"**GeminiBuddy:** {bot_reply}")
