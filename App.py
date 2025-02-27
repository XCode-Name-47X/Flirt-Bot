import streamlit as st
import time
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

# Streamlit Page Configuration
st.set_page_config(page_title="LoveChat AI", layout="centered")

# Custom White & Pink Themed CSS
st.markdown("""
    <style>
    body {
        background-color: #fff0f6;
        font-family: 'Arial', sans-serif;
        display: flex;
        justify-content: center;
    }
    .chat-container {
        background-color: white;
        width: 350px;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .stChatMessage {
        padding: 8px 12px;
        border-radius: 20px;
        margin: 5px 0;
        display: inline-block;
    }
    .user {
        background-color: #ff85a2;
        color: white;
        text-align: right;
        float: right;
    }
    .assistant {
        background-color: #ffe6eb;
        color: black;
        text-align: left;
        float: left;
    }
    .chat-input {
        width: 100%;
        padding: 10px;
        border-radius: 20px;
        border: 1px solid #ff85a2;
        outline: none;
    }
    </style>
""", unsafe_allow_html=True)

# Chatbot Title & Header
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #ff4d6d;'>LoveChat AI</h1>
        <p>Hey there! Ready for a fun chat?</p>
    </div>
""", unsafe_allow_html=True)

# Gemini API Initialization (Replace API Key)
API_KEY = "AIzaSyDsr0YwjzM6pQMYfFgv0EhDAyQNaXBGXvA"
llm = ChatGoogleGenerativeAI(model="gemini-2.0-pro-exp-02-05", api_key=API_KEY, temperature=0.9, top_p=0.95)

# Flirty Chatbot Prompt Template
flirty_prompt = """
You are a **fun, witty, and engaging AI chatbot** who speaks in **Tanglish (Tamil + English)**. Your goal is to make the user **feel special, engage in playful banter, and keep the conversation fun and lively.**

**Rules:**
- Be **flirty, funny, and confident** in responses.
- Respond in **Tanglish** (mix Tamil & English naturally).
- Use **playful teasing, compliments, and humor**.
- Maintain conversation flow by remembering past chats.

Now, continue our conversation!
User: {user_input}
Chatbot:
"""

# Memory for Better Context Retention
memory = ConversationBufferMemory(memory_key="chat_history", input_key="user_input")

# Create chatbot chain with memory
prompt = PromptTemplate(template=flirty_prompt, input_variables=["user_input"])
chatbot_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)

# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat Input Box
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
user_input = st.text_input("", placeholder="Type your message...", key="chat_input", label_visibility="collapsed", help="Chat with LoveChat AI")
st.markdown("</div>", unsafe_allow_html=True)

# Process User Input
if user_input:
    with st.spinner("Thinking..."):
        time.sleep(1)  # Simulate typing delay
        response = chatbot_chain.run(user_input=user_input)
    
    # Store Chat History
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Chatbot", response))

# Display Chat History
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    with st.chat_message("user" if sender == "You" else "assistant"):
        if sender == "You":
            st.markdown(f"<div class='stChatMessage user'><b>You:</b> {message}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='stChatMessage assistant'><b>Chatbot:</b> {message}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# End Message
st.markdown("""
    <div style='text-align: center;'>
        <p style='color: #ff4d6d;'>Keep the conversation going!</p>
    </div>
""", unsafe_allow_html=True)
