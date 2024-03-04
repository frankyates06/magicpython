import streamlit as st
import genai  # Assuming you have installed the genai library

  # Safety settings (optional)
  safety_settings = {
      "profanity_filter": True,  # Adjust settings as needed
      "hate_speech_filter": True
  }

  def analyze_and_respond(image, question):
      """Analyzes the image using Gemini Vision and responds to the question."""

      try:
          model = genai.GenerativeModel('gemini-pro-vision', safety_settings=safety_settings)
          response = model.generate_content(["Observe the image and reply that your magic power will enable you to guess what's in the user's mind, thanks to a very particular detail visible in the photo.", image], stream=True)
          response.resolve()

          for candidate in response.candidates:
              answer = part.text for part in candidate.content.parts
              st.write(answer)
              break  # Display only the first response

      except Exception as e:
          st.error(f"An error occurred: {e}")

  # Streamlit app layout
  st.title("Magic Mind Reader with Gemini Vision")
  st.write("Ask a question about the image, and I'll use my magic powers (powered by Gemini) to guess your thoughts based on a detail I see!")

  uploaded_file = st.file_uploader("Upload an Image")

  if uploaded_file is not None:
      image = st.image(uploaded_file, width=400)  # Adjust width as needed
      question = st.text_input("What's on your mind?")

      if question and st.button("Reveal My Thoughts"):
          analyze_and_respond(image, question)
