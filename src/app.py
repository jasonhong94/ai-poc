import streamlit as st
from streamlit_option_menu import option_menu

from modules.navigation import Navigation
from views import home, chat

def reload_module(module_name):
    import importlib
    import sys
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])
    return sys.modules[module_name]

navigation_module = reload_module('modules.navigation')
Navigation = navigation_module.Navigation
nav = Navigation()

#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Sale | Chat-Bot 🤖")

# deisplay the siderbar menu
menu = nav.nav_menu()
nav.show_menu(menu)

# siderbar_selected = nav.siderbar_menu()
# body_slected = nav.body_menu()

# if siderbar_selected == body_slected == "Home":
#     home.home_page()

# elif siderbar_selected == "Chat": 
#     chat.chat()

# else:
#     st.write("settings is my bettings")


