import os
import sys
import re
from io import StringIO
import streamlit as st
from modules.sidebar import Sidebar
from modules.layout import Layout
from modules.utils import Utilities
from modules.history import ChatHistory


#To be able to update the changes made to modules in localhost (press r)
def reload_module(module_name):
    import importlib
    import sys
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])
    return sys.modules[module_name]

sidebar_module = reload_module('modules.sidebar')
layout_module = reload_module('modules.layout')
utils_module = reload_module('modules.utils')
history_module = reload_module('modules.history')

Sidebar = sidebar_module.Sidebar
Layout = layout_module.Layout
Utilities = utils_module.Utilities
ChatHistory = history_module.ChatHistory

#Config
# st.set_page_config(layout="wide", page_icon="💬", page_title="VSales | Chat-Bot 🤖")

def chat():
# Instantiate the main components
    sidebar, layout, utils, history = Sidebar(), Layout(), Utilities(), ChatHistory()

    layout.show_header("PDF, TXT, CSV")

#get your openai api key
    user_api_key = utils.load_api_key()

#check openai api key 
    if not user_api_key:
        layout.show_api_key_missing()
        exit()
    else:

        os.environ["OPENAI_API_KEY"] = user_api_key

        uploaded_file = utils.handle_upload(["csv", "txt", "pdf"])

        if uploaded_file:
        # Configure the sidebar
            sidebar.show_options()

        # Initiallize chat history

            try:
                chatbot = utils.setup_chatbot(
                    uploaded_file, st.session_state["model"], st.session_state["temperature"]
                )
                st.session_state["chatbot"] = chatbot

                if st.session_state["ready"]:

                # Create containers for chat responses and user prompts
                    response_container, prompt_container = st.container(), st.container()

                    with prompt_container:
                    # Display the prompt form
                        is_ready, user_input = layout.prompt_form()

                    # Initialize the chat history
                        history.initialize(uploaded_file)

                    # Reset the chat history if button clicked
                        if st.session_state["reset_chat"]:
                            history.reset(uploaded_file)

                        if is_ready:
                        # Update the chat history and display the chat messages
                            history.append("user", user_input)

                            old_stdout = sys.stdout
                            sys.stdout = captured_output = StringIO()

                            output = st.session_state["chatbot"].conversational_chat(user_input)

                            sys.stdout = old_stdout

                            history.append("assistant", output)

                        # Clean up the agent's thoughts to remove unwanted characters
                            thoughts = captured_output.getvalue()
                            cleaned_thoughts = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', thoughts)
                            cleaned_thoughts = re.sub(r'\[1m>', '', cleaned_thoughts)

                        # Display the agent's thoughts
                            with st.expander("Display the agent's thoughts"):
                                st.write(cleaned_thoughts)

                        history.generate_messages(response_container)

            except Exception as e:
                st.error(f"Error: {str(e)}")
