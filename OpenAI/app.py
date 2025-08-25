import streamlit as st
import os
from openai import OpenAI

class ChatGPTDashboard:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.initialize_session_state()
        self.setup_sidebar()
        self.display_previous_messages()
        self.handle_user_input()

    def initialize_session_state(self):
        if "model" not in st.session_state:
            st.session_state["model"] = self.client

        if "messages" not in st.session_state:
            st.session_state["messages"] = []

    def setup_sidebar(self):
        st.sidebar.title("Model Parameters")
        self.temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.1)
        self.max_tokens = st.sidebar.slider("Max Tokens", min_value=1, max_value=4096, value=256)

    def display_previous_messages(self):
        for message in st.session_state["messages"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def handle_user_input(self):
        if prompt := st.chat_input("Enter your query"):
            st.session_state["messages"].append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            self.get_response(prompt)

    def get_response(self, prompt):
        with st.chat_message("assistant"):
            stream = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": message["role"], "content": message["content"]} for message in st.session_state["messages"]
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                stream=True
            )
            response = st.write_stream(stream)
        st.session_state["messages"].append({"role": "assistant", "content": response})

if __name__ == "__main__":
    st.title("ChatGPT Dashboard")
    app = ChatGPTDashboard()
