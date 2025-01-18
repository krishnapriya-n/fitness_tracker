import streamlit as st
import openai
import os
import random
from app.responses import generic_responses

# Set OpenAI API key
openai.api_key = 'YOUT_OPEN_API_KEY'

# Function to filter health-related questions
def is_health_related(query):
    health_keywords = [
        "calories", "nutrition", "protein", "workout", "fitness", "macros",
        "diet", "exercise", "health", "food", "meal"
    ]
    return any(keyword in query.lower() for keyword in health_keywords)

# Function to get chatbot's response
def get_chatbot_response(user_message):
    if is_health_related(user_message):
        try:
            # Use OpenAI's API for health-related responses
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Answer the following health and fitness question: {user_message}",
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return "Sorry, I couldn't retrieve the information at this moment."
    else:
        # Return a random generic response for non-health-related questions
        return random.choice(generic_responses)

# Function to handle chatbot interaction
def chatbot():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    st.title("Health & Fitness Chatbot")

    # Display chat history
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.markdown(f"**You**: {message['message']}")
        else:
            st.markdown(f"**AI**: {message['message']}")

    # Input for user message
    user_message = st.text_input("Ask me about fitness, nutrition, or health...", key="user_input")

    # Handle submit
    if st.button("Send"):
        if user_message:
            # Append user message to chat history
            st.session_state.chat_history.append({'role': 'user', 'message': user_message})

            # Get AI response
            ai_response = get_chatbot_response(user_message)

            # Append AI response to chat history
            st.session_state.chat_history.append({'role': 'ai', 'message': ai_response})

            # Clear input field (indirectly reset by Streamlit)
            st.session_state.user_input = ""

    # Button to reset chat history
    if st.button("Reset Chat"):
        st.session_state.chat_history = []

# Run chatbot function
if __name__ == "__main__":
    chatbot()
