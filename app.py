import streamlit as st
import os
import google.generativeai as genai

# Set your API key
GOOGLE_API_KEY = st.secrets["G2API"]

# Configure the SDK with your API key
genai.configure(api_key=GOOGLE_API_KEY)

def ask_animal_poem(animal_name):
    # Initialize the model for a chat
    chat = genai.GenerativeModel('gemini-pro').start_chat()

    # Sending the animal name to start the conversation
    response = chat.send_message(animal_name)

    # Generating a poem based on the animal name
    poem_response = chat.send_message("en quatre  lignes fais un petit poeme qui dit que grace a cette simple reponse l'ordinateur a telepathiquement deviné le mot caché !")
    return poem_response.text

# Streamlit app layout
st.title('Animal Poem Generator')

# User input
animal_name = st.text_input("Enter the name of an animal:")

if st.button('Generate Poem'):
    if animal_name:
        poem = ask_animal_poem(animal_name)
        st.markdown(f"### Generated Poem:\n{poem}", unsafe_allow_html=True)
    else:
        st.write("Please enter the name of an animal to generate a poem.")
