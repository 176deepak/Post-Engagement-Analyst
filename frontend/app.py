import requests
import streamlit as st

st.title("Social Media Engagement Analyst")
st.caption("A LLM agent which can analyze the social media data/data and generate insights.")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi there!"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    payload = {
        "msg": prompt
    }
    response = requests.post("http://127.0.0.1:8000/ask-to-analyzer", json=payload, headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        response = response.json()
        msg = response["message"]
    else:
        msg = "Server Error!"
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)