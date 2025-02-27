import streamlit as st
import time
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

# Streamlit Page Configuration
st.set_page_config(page_title="Tanglish LoveBot 💖", layout="centered")

# Custom Love-Themed CSS for Styling
st.markdown("""
    <style>
    body {
        background: url('img') no-repeat center center fixed;
        background-size: cover;
        font-family: 'Arial', sans-serif;
    }
    .stChatMessage {
        padding: 10px;
        border-radius: 15px;
    }
    .user {
        background-color: #ff007f;
        color: white;
        text-align: right;
        padding: 10px;
        border-radius: 15px;
        max-width: 70%;
        align-self: flex-end;
    }
    .assistant {
        background-color: #ffd9e6;
        color: black;
        padding: 10px;
        border-radius: 15px;
        max-width: 70%;
        align-self: flex-start;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        width: 100%;
    }
    .heart {
        color: #ff007f;
    }
    .message-box {
        background-color: #fff;
        padding: 10px;
        border-radius: 25px;
        width: 100%;
    }
    .chat-input {
        border-radius: 25px;
        border: 2px solid #ff007f;
        padding: 10px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Chatbot Title & Header
st.markdown("<h1 style='text-align: center; color: #ff007f;'>💖 Tanglish LoveBot 😘🔥</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Hey Cutie! Pesalama? 😉💬</h4>", unsafe_allow_html=True)

# Gemini API Initialization (Replace API Key)
API_KEY = "YOUR_GEMINI_API_KEY"  # Replace securely
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=API_KEY, temperature=0.9, top_p=0.95)

# Flirty Chatbot Prompt Template
flirty_prompt = """
You are a **fun, witty, and flirty AI chatbot** who speaks in **Tanglish (Tamil + English)**. Your goal is to make the user **feel special, engage in playful banter, and keep the conversation fun and romantic.**  

💖 **Rules:**  
- Be **flirty, funny, and confident** in responses.  
- Respond in **Tanglish** (mix Tamil & English naturally).  
- Use **playful teasing, compliments, and humor**.  
- Keep the chat engaging like a **romantic comedy**.  
- Maintain conversation flow by remembering past chats.  

Now, continue our conversation!  
User: {user_input}  
Chatbot:
"""

# Add Memory for Context Retention
memory = ConversationBufferMemory(memory_key="chat_history", input_key="user_input")

# Create chatbot chain with memory
prompt = PromptTemplate(template=flirty_prompt, input_variables=["user_input"])
chatbot_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)

# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat Input Box
st.markdown("<h4>💬 Your Message:</h4>", unsafe_allow_html=True)
user_input = st.text_input(" ", placeholder="Type something romantic... 😘", label_visibility="collapsed")

# Process User Input
if user_input:
    with st.spinner("Thinking... 😍"):
        time.sleep(1)  # Simulate typing delay
        response = chatbot_chain.run(user_input=user_input)
    
    # Store Chat History
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Chatbot", response))

# Display Chat History
st.markdown("<h4>💞 Chat History:</h4>", unsafe_allow_html=True)
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    bubble_class = "user" if sender == "You" else "assistant"
    st.markdown(f"<div class='{bubble_class}'><b>{sender}:</b> {message}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# End Message
st.markdown("<h5 style='text-align: center; color: #ff007f;'>💖 Let's keep flirting! 😉🔥</h5>", unsafe_allow_html=True)
