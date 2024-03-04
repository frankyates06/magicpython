import os

# Assuming google.generativeai is a fictional library for this example
import google.generativeai as genai

# Load API key from environment variables
GOOGLE_API_KEY = os.getenv("GAPI")
if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Please set the GAPI environment variable.")

# Configure the genai client with the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Safety settings
safety_settings = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

def generate_poem(object_name):
    """Generates a poem about the given object."""
    try:
        # Assuming GenerativeModel and generate_content work as described for simplicity
        model = genai.GenerativeModel('gemini-pro-vision', safety_settings=safety_settings)
        response = model.generate_content(f"Write a witty poem about a {object_name}.")
        response.resolve()
        for candidate in response.candidates:
            # Assuming each candidate has a 'text' property for simplicity
            print(candidate.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask user for the object
    object_name = input("Please type an object for the poem: ")
    generate_poem(object_name)
