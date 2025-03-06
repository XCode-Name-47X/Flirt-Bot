import streamlit as st

# Custom CSS for animation
st.markdown("""
    <style>
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        .animated-text {
            font-size: 24px;
            font-weight: bold;
            color: red;
            animation: bounce 1s infinite;
        }
    </style>
    <p class="animated-text">Hello, Streamlit! 💖</p>
""", unsafe_allow_html=True)
