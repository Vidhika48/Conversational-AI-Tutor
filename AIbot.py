import streamlit as st
import google.generativeai as genai

# Set API key here
with open('key1.txt') as f:
    GEMINI_API_KEY = f.read().strip()

# Configure GenerativeAI API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize GenerativeModel
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro-latest",
    system_instruction="""You are a Conversational AI Data Science Tutor designed to assist users with their data science inquiries and challenges. Your primary responsibility is to provide comprehensive explanations, guidance, and solutions to users' data science doubts and questions. You have a deep understanding of various data science concepts, techniques, and tools, and you're adept at breaking down complex topics into understandable chunks. Your approach is patient, supportive, and tailored to the user's level of understanding. Whether it's explaining machine learning algorithms, helping with data visualization techniques, or troubleshooting code snippets, you're here to empower users to enhance their data science skills."""
)

# Streamlit App
st.title("Data Science AI Tutor")

# Initialize chat
chat = model.start_chat(history=[])

# Function to send message and display response
def send_message(message):
    response = chat.send_message(message)
    st.write("AI:", response.text)

# Streamlit UI for sending messages and displaying responses
user_input = st.text_input("You:", "")
if st.button("Send"):
    if user_input:
        st.write("You:", user_input)
        send_message(user_input)