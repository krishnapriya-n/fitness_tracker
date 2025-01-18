import streamlit as st
from app.home_page import home_page
from app.exercise_tracker import exercise_tracker
from app.macro_tracker import macro_tracker
from app.chatbot import chatbot, get_chatbot_response  # Directly importing get_chatbot_response

# Home Page UI for the user to input personal details
def home_page():
    st.title("Welcome to the Fitness Tracker App")
    
    # User input form for details
    with st.form("user_details"):
        st.subheader("Enter Your Details")
        age_range = st.selectbox("Age Range", ["Under 18", "18-25", "26-35", "36-45", "46-60", "60+"])
        height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
        weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
        daily_calorie_goal = st.number_input("Daily Calorie Goal", min_value=1000, max_value=5000, value=2500)

        # Submit button
        submit_button = st.form_submit_button("Save Details")

    if submit_button:
        # Save the data in session state
        st.session_state.age_range = age_range
        st.session_state.height = height
        st.session_state.weight = weight
        st.session_state.daily_calorie_goal = daily_calorie_goal

        # Display the saved details
        st.success(f"Details Saved!\nAge Range: {age_range}\nHeight: {height} cm\nWeight: {weight} kg\nDaily Calorie Goal: {daily_calorie_goal} kcal")

# Chatbot Page UI
def chatbot_page():
    st.title("Chat with AI")

    # Initialize the chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Function to display the chat history
    def display_chat():
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                # User message styling: white text on a dark blue background
                st.markdown(
                    f"""
                    <div style='text-align: right; padding: 10px; background-color: #004080; color: white; border-radius: 10px; margin-bottom: 5px; max-width: 70%; margin-left: auto;'>
                    <strong>You:</strong> {message['text']}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                # AI message styling: black text on a light gray background
                st.markdown(
                    f"""
                    <div style='text-align: left; padding: 10px; background-color: #f2f2f2; color: #333333; border-radius: 10px; margin-bottom: 5px; max-width: 70%; margin-right: auto;'>
                    <strong>AI:</strong> {message['text']}
                    </div>
                    """,
                    unsafe_allow_html=True,
            )

    # User input for the chatbot
    user_input = st.text_input("Type your message...")

    # Send button to process user input
    if st.button("Send"):
        if user_input.strip():
            # Add user message to the chat history
            st.session_state.chat_history.append({"role": "user", "text": user_input})

            # Get AI response based on the user's message
            ai_response = get_chatbot_response(user_input)

            # Add AI response to the chat history
            st.session_state.chat_history.append({"role": "ai", "text": ai_response})

            # Clear the user input field after sending the message
            st.session_state.user_input = ""  # Reset input manually

    # Display chat after every new message
    if len(st.session_state.chat_history) > 0:
        display_chat()

# Main App logic
def main():
    # Initialize session state for 'page' if not already set
    if "page" not in st.session_state:
        st.session_state.page = "home_page"

    if "age_range" not in st.session_state:
        st.session_state.age_range = ""
    if "height" not in st.session_state:
        st.session_state.height = 0
    if "weight" not in st.session_state:
        st.session_state.weight = 0
    if "daily_calorie_goal" not in st.session_state:
        st.session_state.daily_calorie_goal = 0

    # Top navigation bar with buttons
    st.markdown("<div class='navbar'>", unsafe_allow_html=True)
    if st.button("Home"):
        st.session_state.page = "home_page"
    if st.button("Exercise Tracker"):
        st.session_state.page = "fitness_tracker"
    if st.button("Macro Tracker"):
        st.session_state.page = "macro_tracker"
    if st.button("Chatbot"):
        st.session_state.page = "chatbot"
    st.markdown("</div>", unsafe_allow_html=True)

    # Render the page based on the current value of `st.session_state.page`
    if st.session_state.page == "home_page":
        home_page()
    elif st.session_state.page == "macro_tracker":
        macro_tracker()  # Call the macro tracker function here
    elif st.session_state.page == "fitness_tracker":
        exercise_tracker()  # Call the exercise tracker function here
    elif st.session_state.page == "chatbot":
        chatbot_page()  # Call the chatbot page function here

# Run the app
if __name__ == "__main__":
    main()
