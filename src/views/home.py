import streamlit as st

def home_page():

    container = st.container()
        #Title
    container.markdown(
            """
            <h2 style='text-align: center;'>Welcome to  AI Sales assistant 🤖</h1>
            """,
            unsafe_allow_html=True,)

    container.markdown("---")

        #Description
    container.markdown(
            """ 
            <h5 style='text-align:justify;'>I'm VSalesBot, an intelligent chatbot created by VCIG Limited. </h5>
    
            <h5 style='text-align:justify;'>I use large language models to provide context-sensitive interactions with combining the langchain and streamlit. </h5>
            <h5 style='text-align:justify;'>My life purpose is to help people better understand Merchant product/profile and easy to order. 🧠 </h5>
    
            """,
            unsafe_allow_html=True)
    
    container.markdown("---")