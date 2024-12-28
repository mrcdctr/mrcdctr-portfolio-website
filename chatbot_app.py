from transformers import pipeline
import streamlit as st

chatbot = pipeline('text-generation', model='gpt2')

st.title("Simple AI Chatbot")
st.subheader("Chat with a GPT-2 powered bot")

user_input = st.text_input("Ask me anything:")

if st.button("Chat"):
    if user_input:
        response = chatbot(user_input, max_length=50, num_return_sequences=1)
        st.write("**Bot:**", response[0]['generated_text'])
    else:
        st.warning("Please enter a question.")
