import streamlit as st
import openai
from streamlit_chat import message

st.title('🧠💬 Streamlit GPT')
openai.api_key = st.secrets.openai_api_key
if 'messages' not in st.session_state:
    st.session_state['messages'] = [{"role": "assistant", "content": "How can I help you?"}]

with st.form("chat_input", clear_on_submit=True):
    user_input = st.text_input("User: ")
    st.form_submit_button("Submit")

for msg in st.session_state.messages:
    message(msg["content"], is_user= msg["role"] == "user")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    message(user_input, is_user=True)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages).choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": response})
    message(response)
