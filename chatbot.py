import os
import streamlit as st
from groq import Groq

# Initialize the Groq client
client = Groq(
    api_key="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",  # Add your Groq API key here
)

# Streamlit app title
st.title("Groq Chatbot")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful and knowledgeable assistant."
        }
    ]

# Display conversation history
for message in st.session_state.messages:
    if message["role"] != "system":  # Skip system message
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Get user input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user input to conversation history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user input in the chat
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get the chatbot's response
    chat_completion = client.chat.completions.create(
        messages=st.session_state.messages,
        model="deepseek-r1-distill-llama-70b",  # Use the desired model
    )

    # Extract the chatbot's reply
    chatbot_reply = chat_completion.choices[0].message.content

    # Add chatbot's reply to conversation history
    st.session_state.messages.append({
        "role": "assistant",
        "content": chatbot_reply
    })

    # Display chatbot's reply in the chat
    with st.chat_message("assistant"):
        st.markdown(chatbot_reply)