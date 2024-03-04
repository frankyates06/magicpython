import os
import google.generativeai as genai

# Set your API key
GOOGLE_API_KEY = os.getenv("GAPI")

# Configure the SDK with your API key
genai.configure(api_key=GOOGLE_API_KEY)

def ask_how_are_you():
    # Initialize the model for a chat
    chat = genai.GenerativeModel('gemini-pro').start_chat()

    # Sending a message to start the conversation
    user_input = input("Donne le nom d'un animal? ")
    response = chat.send_message(user_input)

    # Generating a funny remark based on the user's input
    funny_response = chat.send_message("en quatre  lignes fais un petit poeme qui dit que grace a cette simple reponse l'ordinateur a telepathiquement deviné le mot caché !")
    print(funny_response.text)

ask_how_are_you()