# Fitness Tracker App

This is a simple fitness tracker app built using Streamlit and OpenAI's GPT for chatbot interactions. It allows users to input personal details, track exercise and macro data, and interact with an AI chatbot to get fitness-related advice.

The main code for this app was developed by [Aarnavman](https://github.com/aarnavman) from GitHub. We're collaborating on this project for the United Hacks hackathon.

## Features

- **Home Page**: Users can input their personal information, such as age range, height, weight, and daily calorie goal.
- **Exercise Tracker**: Allows users to log and track their exercises.
- **Macro Tracker**: Helps users keep track of their macronutrients (carbs, fats, proteins).
- **AI Chatbot**: Provides fitness-related advice and answers questions via a conversational interface.

## Requirements

The following libraries are required to run the app:

- `openai`: For interacting with OpenAI's GPT models.
- `streamlit`: For building the interactive web app.
- `requests`: For making HTTP requests.
- `pandas`: For managing and analyzing data.

## Installation

Follow these steps to set up and run the app locally:

### 1. Clone the repository
First, clone this repository to your local machine:
```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Set up a virtual environment (optional but recommended)
A virtual environment ensures that the app runs with the correct dependencies.

- On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

- On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
Once the virtual environment is activated, install the required dependencies by running:
```bash
pip install -r requirements.txt
```

### 4. Set up OpenAI API key
The chatbot uses OpenAI's API to provide responses. To set up:

1. Create an account at OpenAI.
2. Obtain your API key from the OpenAI API Dashboard.
3. Paste the key onto the `chatbot.py` code.

### 5. Set up USDA API key
The macro tracker is made using values from USDA. To set up:
1. Create an account at USDA APIs.
2. Obtain your API key.
3. Paste the key onto the `macro_tracker.py` code.

### 6. Run the app
Once everything is set up, you can run the app locally using Streamlit:
```bash
streamlit run app.py
```

This will launch the app in your default web browser. You can start using it immediately.

## Usage

### Home Page
- Input your age, height, weight, and daily calorie goal.
- These details will be saved and can be used in other sections of the app.

### Exercise Tracker
- Track your exercises by adding data such as the type of exercise, duration, and calories burned.

### Macro Tracker
- Keep track of your daily macronutrient intake (carbs, fats, proteins).

### AI Chatbot
- Chat with the AI about fitness, nutrition, or any questions you may have. The chatbot is powered by OpenAI's GPT and is designed to help with fitness-related queries.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Contributions are always welcome!

### Steps for contributing:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Added new feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Aarnavman for the main code and collaboration on this project for United Hacks.
- OpenAI for providing the GPT model API.
- Streamlit for providing an easy-to-use interface for building web apps.
