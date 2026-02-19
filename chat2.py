import streamlit as st
import google.generativeai as genai

# Configure API key securely
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

def query(user_query):
    try:
        response = model.generate_content(user_query)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


if'message' not in st.session_state:
   st.session_state.message=[]

for i in st.session_state.message:
   with st.chat_message(i["role"]):
      st.markdown(i["msg"])



st.title("chatbot")
user_input=st.chat_input("enter yor query")
# store user msg
if user_input:                            
    st.session_state.message.append({
       "role":"user",
       "msg":user_input
    })
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Thinking"):
           result=query(user_input)
           st.markdown(result)
        #    assistant response
    st.session_state.message.append({
       "role":"assistant",
       "msg":result
    })
        

















