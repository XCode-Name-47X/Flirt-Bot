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
        padding: 10px;
    }
    .chat-bubble {
        padding: 12px;
        border-radius: 15px;
        margin: 5px 0;
        display: inline-block;
        max-width: 75%;
        font-size: 16px;
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
    .chat-input-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 10px;
        padding: 10px;
        background: white;
        border-radius: 15px;
        border: 1px solid #ff6699;
    }
    .input-box {
        flex-grow: 1;
        padding: 10px;
        border: none;
        border-radius: 10px;
        outline: none;
        font-size: 16px;
    }
    .send-btn {
        background-color: #ff3366;
        color: white;
        padding: 10px 15px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        margin-left: 5px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# 🎤 Gemini API Initialization
API_KEY = "AIzaSyDsr0YwjzM6pQMYfFgv0EhDAyQNaXBGXvA"
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=API_KEY, temperature=0.9, top_p=0.95)

# 📝 User Session Setup
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_gender" not in st.session_state:
    st.session_state.user_gender = ""
if "chat_started" not in st.session_state:
    st.session_state.chat_started = False

# 💖 Welcome & User Info Page
if not st.session_state.chat_started:
    st.markdown("""
        <div style='text-align: center;'>
            <h1 style='color: #ff3366;'>💖 Tanglish LoveBot 😘🔥</h1>
            <h4>Hey Cutie! Pesalama? 😉💬</h4>
        </div>
    """, unsafe_allow_html=True)

    with st.form("user_info_form"):
        st.session_state.user_name = st.text_input("💖 Your Name:", placeholder="Ex: Karthi, Meera...")
        st.session_state.user_gender = st.radio("💞 Your Gender:", ["Male", "Female"], index=0)
        submitted = st.form_submit_button("Start Chat 💌")

    if submitted and st.session_state.user_name:
        st.session_state.chat_started = True
        st.experimental_rerun()
else:
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

    # 💞 Chat UI
    st.markdown("""
        <div style='text-align: center;'>
            <h2 style='color: #ff3366;'>💖 Let's Chat, {}</h2>
        </div>
    """.format(st.session_state.user_name), unsafe_allow_html=True)

    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for sender, message in st.session_state.chat_history:
        bubble_class = "user" if sender == "You" else "bot"
        st.markdown(f"<div class='chat-bubble {bubble_class}'><b>{sender}:</b> {message}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 💌 Chat Input Box with Send Button
    st.markdown("<div class='chat-input-container'>", unsafe_allow_html=True)
    user_input = st.text_input("", placeholder="Type something romantic... 😘", key="chat_input", label_visibility="collapsed")
    if st.button("Send 💌", key="send", help="Send your message!"):
        if user_input:
            with st.spinner("Thinking... 😍"):
                time.sleep(1)
                response = chatbot_chain.run(user_input=user_input, user_name=st.session_state.user_name, user_gender=st.session_state.user_gender)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Chatbot", response))
            st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)
