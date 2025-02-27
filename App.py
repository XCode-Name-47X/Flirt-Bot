import streamlit as st
import time
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

# ❤️ Streamlit Page Configuration
st.set_page_config(page_title="Tanglish LoveBot 💖", layout="centered")

# 💕 Custom Love-Themed CSS for Styling
st.markdown("""
    <style>
    body {
        background-color: #ffeff6;
        font-family: 'Arial', sans-serif;
    }
    .stChatMessage {
        padding: 10px;
        border-radius: 15px;
    }
    .user {
        background-color: #ff99cc;
        color: white;
        text-align: right;
    }
    .assistant {
        background-color: #ffd9e6;
        color: black;
    }
    .heart {
        color: #ff007f;
    }
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    </style>
""", unsafe_allow_html=True)

# 💖 Chatbot Title & Header
st.markdown("<h1 style='text-align: center; color: #ff007f;'>💖 Tanglish LoveBot 😘🔥</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Hey Cutie! Pesalama? 😉💬</h4>", unsafe_allow_html=True)

# 📝 Get User Info (Name & Gender)
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_gender" not in st.session_state:
    st.session_state.user_gender = ""

with st.form("user_info_form"):
    st.session_state.user_name = st.text_input("💖 Your Name:", value=st.session_state.user_name, placeholder="Ex: Karthi, Meera...")
    st.session_state.user_gender = st.radio("💞 Your Gender:", ["Male", "Female"], index=0 if st.session_state.user_gender == "Male" else 1)
    submitted = st.form_submit_button("Start Chat 💌")

# 🛑 Don't proceed until user inputs their name & gender
if not st.session_state.user_name:
    st.warning("💖 Pease enter your name to start chatting!")
    st.stop()

# 🎤 Gemini API Initialization (Replace API Key)
API_KEY = "AIzaSyDsr0YwjzM6pQMYfFgv0EhDAyQNaXBGXvA"  # Securely replace with actual key
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=API_KEY, temperature=0.9, top_p=0.95)

# 💌 Flirty Chatbot Prompt Template (Now Personalized)
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

# 🧠 Add Memory for Better Context Retention
memory = ConversationBufferMemory(memory_key="chat_history", input_key="user_input")

# 🔥 Create chatbot chain with memory
prompt = PromptTemplate(template=flirty_prompt, input_variables=["user_input", "user_name", "user_gender"])
chatbot_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)

# 📝 Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 💌 Love-Themed Chat Input Box
st.markdown(f"<h4>💬 {st.session_state.user_name}, Your Message:</h4>", unsafe_allow_html=True)
user_input = st.text_input(" ", placeholder="Type something romantic... 😘", label_visibility="collapsed")

# 🚀 Process User Input
if user_input:
    with st.spinner("Thinking... 😍"):
        time.sleep(1)  # Simulate typing delay
        response = chatbot_chain.run(user_input=user_input, user_name=st.session_state.user_name, user_gender=st.session_state.user_gender)
    
    # Store Chat History
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Chatbot", response))

# 🥰 Display Chat History
st.markdown("<h4>💞 Chat History:</h4>", unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    with st.chat_message("user" if sender == "You" else "assistant"):
        if sender == "You":
            st.markdown(f"<div class='stChatMessage user'><b>You:</b> {message} 😘</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='stChatMessage assistant'><b>Chatbot:</b> {message} ❤️</div>", unsafe_allow_html=True)

# 🔚 End Message
st.markdown(f"<h5 style='text-align: center; color: #ff007f;'>💖 {st.session_state.user_name}, Let's keep flirting! 😉🔥</h5>", unsafe_allow_html=True)
