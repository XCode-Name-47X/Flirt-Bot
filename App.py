import streamlit as st
import time
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

# ❤️ Streamlit Page Configuration
st.set_page_config(page_title="Neera 💖", layout="centered")



# 💖 Chatbot Title & Header
st.markdown("<h1 style='text-align: center; color: #ff007f;'>Neeraa 💖</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Hey Cutie! Pesalama? 😉💬</h4>", unsafe_allow_html=True)

# 🎤 Gemini API Initialization (Replace API Key)
API_KEY = "AIzaSyDsr0YwjzM6pQMYfFgv0EhDAyQNaXBGXvA"  # Securely replace with actual key
llm = ChatGoogleGenerativeAI(model="gemini-2.0-pro-exp-02-05", api_key=API_KEY, temperature=0.9, top_p=0.95)

# 💌 Flirty Chatbot Prompt Template
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

# 🧠 Add Memory for Better Context Retention
memory = ConversationBufferMemory(memory_key="chat_history", input_key="user_input")

# 🔥 Create chatbot chain with memory
prompt = PromptTemplate(template=flirty_prompt, input_variables=["user_input"])
chatbot_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)

# 📝 Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 💌 Love-Themed Chat Input Box
st.markdown("<h4>💬 Your Message:</h4>", unsafe_allow_html=True)
user_input = st.text_input(" ", placeholder="Type something romantic... 😘", label_visibility="collapsed")

# 🚀 Process User Input
if user_input:
    with st.spinner("Thinking... 😍"):
        time.sleep(1)  # Simulate typing delay
        response = chatbot_chain.run(user_input=user_input)
    
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
st.markdown("<h5 style='text-align: center; color: #ff007f;'>💖 Let's keep flirting! 😉🔥</h5>", unsafe_allow_html=True)
