import streamlit as st
def query(user_query):   
    from google import genai

    api_key="AIzaSyChK_SaHXGSAYUr5Xsouf-yKNKUiFlu604"
    my_ai = genai.Client(api_key = api_key)
    response=my_ai.models.generate_content(
            model="gemini-1.5-flash",
            contents=user_query
    )
    return(response.text)


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
        





