import streamlit as st
import time

# Add custom CSS
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
        .exercise-title {
            font-size: 1.5em;
            font-weight: bold;
            margin-bottom: 15px;
        }
        .timer {
            font-size: 2em;
            font-weight: bold;
            color: #fefefe;
            margin: 20px 0;
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
        </style>
    """, unsafe_allow_html=True)

# Calculate calories burned for each exercise
def calculate_calories_burned(weight, exercise_type, duration):
    calories_per_minute = {
        "running": 0.074,
        "jumping_jacks": 0.053,
        "pushups": 0.045
    }
    return calories_per_minute.get(exercise_type, 0) * weight * duration

# Exercise Card
def exercise_card(exercise_name, total_reps, duration_seconds, exercise_id, weight):
    st.markdown(f'<div class="card"><div class="exercise-title">{exercise_name}</div>', unsafe_allow_html=True)

    completed_reps = 0
    elapsed_seconds = 0
    calories_burned = 0

    while elapsed_seconds < duration_seconds and completed_reps < total_reps:
        # Update Timer and Reps Completed
        elapsed_minutes, elapsed_seconds_display = divmod(elapsed_seconds, 60)
        st.markdown(f'<div class="timer">{int(elapsed_minutes):02d}:{int(elapsed_seconds_display):02d}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="timer">Completed Reps: {completed_reps}/{total_reps}</div>', unsafe_allow_html=True)

        # Simulate reps and time
        time.sleep(1)
        elapsed_seconds += 1
        completed_reps += 1

        # Track calories burned
        calories_burned = calculate_calories_burned(weight, exercise_name, elapsed_seconds / 60)  # per minute

        # Clear content for the next update
        st.empty()

    # Completion Message
    st.markdown(f'<div class="timer">Exercise Completed! Calories Burned: {calories_burned:.2f} kcal</div>', unsafe_allow_html=True)

    # Add buttons for removing the exercise
    if st.button(f"Remove {exercise_name}", key=exercise_id):
        st.session_state.exercises = [exercise for exercise in st.session_state.exercises if exercise["id"] != exercise_id]

    st.markdown('</div>', unsafe_allow_html=True)

# Main Exercise Tracker
def exercise_tracker():
    add_custom_css()
    st.header("Exercise Tracker")

    # Session state for exercises
    if "exercises" not in st.session_state:
        st.session_state.exercises = []

    # Add new exercise form
    with st.form("add_exercise"):
        st.header("Add a New Exercise")
        exercise_name = st.text_input("Exercise Name", value="Push-ups")
        total_reps = st.number_input("Total Reps", min_value=1, value=10, step=1)
        duration_minutes = st.number_input("Duration (in minutes)", min_value=1, value=1, step=1)
        duration_seconds = int(duration_minutes * 60)
        weight = st.number_input("Your Weight (kg)", min_value=1, value=70)

        if duration_seconds <= 0:
            st.error("Duration must be greater than 0.")
        else:
            add_exercise = st.form_submit_button("Add Exercise")

            if add_exercise:
                exercise_id = len(st.session_state.exercises) + 1
                st.session_state.exercises.append({
                    "id": exercise_id,
                    "name": exercise_name,
                    "reps": total_reps,
                    "duration_seconds": duration_seconds,
                    "weight": weight
                })
                st.success(f"Added {exercise_name} successfully!")

    # Display all added exercises
    if st.session_state.exercises:
        for exercise in st.session_state.exercises:
            exercise_card(
                exercise["name"],
                exercise["reps"],
                exercise["duration_seconds"],
                exercise["id"],
                exercise["weight"]
            )

# Run the Exercise Tracker
if __name__ == "__main__":
    exercise_tracker()
