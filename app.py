import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
import openai
import os
import base64
import time 
# Set your OpenAI API key here
openai_api_key = "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"

# Initialize the OpenAI API
openai.api_key = openai_api_key

# Define the local path to your image
image_path = "C:/Users/Haseeb Raza/Desktop/pdf_Model/bg3.jpg"
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
encoded_image = get_base64_of_bin_file(image_path)
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('data:image/jpg;base64,{encoded_image}');
        background-size: cover;
        color: white;
    }}
    .stApp {{
        background-color: transparent;
    }}
    .title {{
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        font-weight: bold;
    }}
     
    """,
    unsafe_allow_html=True
)
def display_about_us():
    st.title("About Me")
    st.write("CS Sophomore@ INFORMATION TECHNOLOGY UNIVERSITY")
   


load_dotenv()

def main():
    st.header("🦜️🔗Chat with PDF 💬--Made with ❤️by Haseeb Raza")

    # upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Ask user for a question
        query = st.text_input("Ask questions about your PDF file:")

        if query:
            try:
                # Call the OpenAI API to generate a response
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": text},
                        {"role": "user", "content": query}
                    ]
                )
                
                # Check if the response is not empty
                if response['choices']:
                    # Iterate over choices and print each message
                    for choice in response['choices']:
                        if 'message' in choice and 'content' in choice['message']:
                            message_content = choice['message']['content']
                            trimmed_message = message_content.strip()
                            st.write(trimmed_message)
                else:
                    st.write("No response from the model.")
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
    display_about_us()
    # Hide the "About Us" content after 5 seconds
    
