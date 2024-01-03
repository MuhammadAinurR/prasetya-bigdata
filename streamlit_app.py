import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key='AIzaSyAPcjYLQmj0k2Wzy1pP7U1Hdjnb0BOHMVI')

# Set default parameters
defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

st.title('Ask Me')
st.write('You can ask anythings code')
final_response = None
# Creating a side panel for inputs
with st.sidebar:
    st.write("## Input Code")
    # Create a dropdown for selecting the programming language
   
    # Create a text input for the prompt
    prompt = st.text_area("What`s your problem")
    # When the 'Generate' button is pressed, generate the text
    if st.button('Generate'):
        formatted_prompt = f"explain this code with details {prompt}"
        response = genai.generate_text(
            **defaults,
            prompt=formatted_prompt
        )
        final_response = response
if final_response != None:
    st.write(final_response.result)
