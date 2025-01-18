import requests
import streamlit as st
import pandas as pd

# USDA API endpoint and your API key (replace with your actual API key)
USDA_API_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"
USDA_API_KEY = "YOUR_API_KEY"  # Replace with your API key

# Function to fetch food data from USDA
def fetch_food_data(food_name):
    params = {
        "query": food_name,
        "api_key": USDA_API_KEY,
        "pageSize": 1  # Get only the first result (modify as needed)
    }
    response = requests.get(USDA_API_URL, params=params)
    
    if response.status_code == 200:
        food_data = response.json()
        if food_data["foods"]:
            food_info = food_data["foods"][0]
            food_nutrients = food_info.get("foodNutrients", [])
            
            # Extract nutrients (if available)
            nutrients = {
                "calories": 0,
                "protein": 0,
                "carbs": 0,
                "fats": 0
            }
            for nutrient in food_nutrients:
                if nutrient["nutrientName"] == "Energy":
                    nutrients["calories"] = nutrient["value"]
                elif nutrient["nutrientName"] == "Protein":
                    nutrients["protein"] = nutrient["value"]
                elif nutrient["nutrientName"] == "Carbohydrate, by difference":
                    nutrients["carbs"] = nutrient["value"]
                elif nutrient["nutrientName"] == "Total lipid (fat)":
                    nutrients["fats"] = nutrient["value"]
            
            return nutrients
        else:
            return None
    else:
        st.error("Error fetching data from USDA API.")
        return None

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
        .add-button, .remove-button {
            font-size: 1.5em;
            font-weight: bold;
            color: white;
            background-color: #E74C3C;
            border: none;
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
        }
        .add-button:hover, .remove-button:hover {
            background-color: #C0392B;
        }
        .input-group {
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

# Macro Tracker Form
def macro_tracker():
    add_custom_css()  # Add custom CSS
    st.header("Macro Tracker")

    # Initialize session state variables if not already set
    if "macros" not in st.session_state:
        st.session_state.macros = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}
    
    # Initialize caloric_goal if not already set
    if "caloric_goal" not in st.session_state:
        st.session_state.caloric_goal = 0  # Set a default value for the goal (can be changed by user)

    # Add new food intake
    with st.form("add_food"):
        st.subheader("Add Food Intake")
        food_name = st.text_input("Food Name", value="Apple")
        
        # Fetch nutritional information from USDA
        if food_name:
            food_data = fetch_food_data(food_name)
            if food_data:
                calories = food_data["calories"]
                protein = food_data["protein"]
                carbs = food_data["carbs"]
                fats = food_data["fats"]
            else:
                calories = protein = carbs = fats = 0
                st.warning(f"Could not find nutritional data for {food_name}.")
        
        submit_food = st.form_submit_button("Add Food")

        if submit_food:
            st.session_state.macros["calories"] += calories
            st.session_state.macros["protein"] += protein
            st.session_state.macros["carbs"] += carbs
            st.session_state.macros["fats"] += fats
            st.success(f"Added {food_name} successfully with {calories} kcal.")

    # Display current macro status
    st.subheader("Current Macro Status")
    st.write(f"Calories: {st.session_state.macros['calories']} / Goal: {st.session_state.caloric_goal} kcal")
    st.write(f"Protein: {st.session_state.macros['protein']} g")
    st.write(f"Carbs: {st.session_state.macros['carbs']} g")
    st.write(f"Fats: {st.session_state.macros['fats']} g")

    # Option to remove food intake
    if st.button("Remove Last Food Intake"):
        st.session_state.macros = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}

if __name__ == "__main__":
    macro_tracker()
