import streamlit as st
import math

if "page" not in st.session_state:
    st.session_state.page = "home_page"


# Add custom CSS for styling
def add_custom_css():
    st.markdown("""
        <style>
        .card {
            background-color: #1ABC9C;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            color: white;
            font-family: 'Poppins', sans-serif;
            text-align: center;
            margin: 20px auto;
            max-width: 400px;
        }
        .card-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .card-button {
            font-size: 1.2em;
            font-weight: bold;
            color: white;
            background-color: #3498DB;
            border: none;
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
        }
        .card-button:hover {
            background-color: #2980B9;
        }
        .input-group {
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

# Function to calculate BMR and caloric goal
def calculate_bmr(age, weight, height, gender='male'):
    if gender == 'male':
        return 66 + (13.75 * weight) + (5 * height) - (6.75 * age)
    else:
        return 655 + (9.56 * weight) + (1.85 * height) - (4.68 * age)

# Home Page Layout
def home_page():
    st.title("Fitness and Macro Tracker")
    
    # Initialize session_state variables if not already set
    if 'caloric_goal' not in st.session_state:
        st.session_state.caloric_goal = 0  # Default to 0

    # User Input
    st.subheader("Enter Your Details")
    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    height = st.number_input("Height (cm)", min_value=1, max_value=250, value=170)
    weight = st.number_input("Weight (kg)", min_value=1, max_value=200, value=70)
    gender = st.selectbox("Gender", ["male", "female"])
    
    # Calculate BMR (Basal Metabolic Rate) to estimate daily calories
    bmr = calculate_bmr(age, weight, height, gender)
    caloric_goal = st.number_input("Goal Calories for the Day", min_value=1, value=int(bmr * 1.2), step=100)
    
    # Store caloric_goal in session state
    st.session_state.caloric_goal = caloric_goal
    st.session_state.bmr = bmr  # Also storing BMR in session state for use in other pages
    
    st.write(f"Estimated BMR: {bmr} kcal/day")
    
    # Display the cards linking to Fitness Tracker, Macro Tracker, and Chatbot
    st.subheader("Quick Access")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Fitness Tracker"):
            st.session_state.page = "fitness_tracker"
    with col2:
        if st.button("Macro Tracker"):
            st.session_state.page = "macro_tracker"
    with col3:
        if st.button("Talk to our AI"):
            st.session_state.page = "chatbot"  # Redirect to chatbot page
    
    st.write(f"Your caloric goal for today: {caloric_goal} kcal")
    st.write(f"Remaining Calories: {caloric_goal} kcal")


# Navigate between pages
if st.session_state.page == "macro_tracker":
    import macro_tracker
    macro_tracker.macro_tracker()
elif st.session_state.page == "chatbot":
    import chatbot
    chatbot.chatbot()
    
if __name__ == "__main__":
    home_page()
