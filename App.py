import streamlit as st
import time
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

# ❤️ Streamlit Page Configuration
st.set_page_config(page_title="Tanglish LoveBot 💖", layout="centered")

# 💕 Custom Love-Themed CSS for UI Styling
st.markdown("""
    <style>
    body {
        background-color: #ffe6f2;
        font-family: 'Arial', sans-serif;
    }
    .chat-container {
        max-width: 400px;
        margin: auto;
    }
    .chat-bubble {
        padding: 12px;
        border-radius: 20px;
        margin: 5px 0;
        display: inline-block;
        max-width: 80%;
    }
    .user {
        background-color: #ff3366;
        color: white;
        text-align: right;
        float: right;
    }
    .bot {
        background-color: #ffccd5;
        color: black;
        float: left;
    }
    .input-box {
        width: 100%;
        padding: 10px;
        border-radius: 15px;
        border: 1px solid #ff6699;
        margin-top: 10px;
    }
    .send-btn {
        background-color: #ff3366;
        color: white;
        padding: 10px 15px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# 💖 Chatbot Title & Header
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #ff3366;'>💖 Tanglish LoveBot 😘🔥</h1>
        <h4>Hey Cutie! Pesalama? 😉💬</h4>
    </div>
""", unsafe_allow_html=True)

# 📝 Get User Info (Name & Gender)
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_gender" not in st.session_state:
    st.session_state.user_gender = ""

with st.form("user_info_form"):
    st.session_state.user_name = st.text_input("💖 Your Name:", value=st.session_state.user_name, placeholder="Ex: Karthi, Meera...")
    st.session_state.user_gender = st.radio("💞 Your Gender:", ["Male", "Female"], index=0 if st.session_state.user_gender == "Male" else 1)
    submitted = st.form_submit_button("Start Chat 💌")

if not st.session_state.user_name:
    st.warning("💖 Pease enter your name to start chatting!")
    st.stop()

# 🎤 Gemini API Initialization
API_KEY = "AIzaSyDsr0YwjzM6pQMYfFgv0EhDAyQNaXBGXvA"
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=API_KEY, temperature=0.9, top_p=0.95)

# 💌 Flirty Chatbot Prompt Template
flirty_prompt = """
You are a **fun, witty, and flirty AI chatbot** who speaks in **Tanglish (Tamil + English)**. Your goal is to make the user **feel special, engage in playful banter, and keep the conversation fun and romantic.**  

👤 **User Details:**  
- **Name:** {user_name}  
- **Gender:** {user_gender}  

💖 **Rules:**  
- Be **flirty, funny, and confident** in responses.  
- Respond in **Tanglish** (mix Tamil & English naturally).  
- Use **playful teasing, compliments, and humor**.  
- Adjust responses based on the **user's gender** (e.g., call a guy "Thalaiva" & a girl "Chellam").  
- Keep the chat engaging like a **romantic comedy**.  
- Maintain conversation flow by remembering past chats.  

Now, continue our conversation!  
User: {user_input}  
Chatbot:
"""

# 🧠 Add Memory for Context Retention
memory = ConversationBufferMemory(memory_key="chat_history", input_key="user_input")
prompt = PromptTemplate(template=flirty_prompt, input_variables=["user_input", "user_name", "user_gender"])
chatbot_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)

# 📝 Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 🎤 Chat Input
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
user_input = st.text_input(" ", placeholder="Type something romantic... 😘", key="chat_input", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if st.button("Send 💌", key="send", help="Send your message!"):
    if user_input:
        with st.spinner("Thinking... 😍"):
            time.sleep(1)
            response = chatbot_chain.run(user_input=user_input, user_name=st.session_state.user_name, user_gender=st.session_state.user_gender)
        
        # Store Chat History
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Chatbot", response))

# 🥰 Display Chat History
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"<div class='chat-bubble user'><b>You:</b> {message} 😘</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble bot'><b>Chatbot:</b> {message} ❤️</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 🔚 End Message
st.markdown(f"<h5 style='text-align: center; color: #ff3366;'>💖 {st.session_state.user_name}, Let's keep flirting! 😉🔥</h5>", unsafe_allow_html=True)
