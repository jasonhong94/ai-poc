import streamlit as st
from streamlit_option_menu import option_menu
from st_on_hover_tabs import on_hover_tabs
from views import home, chat

class Navigation:

    # 1. as sidebar menu
    # def siderbar_menu(self): 
    #     with st.sidebar:
    #         selected = option_menu("Main Menu", ["Home", 'Chat','Settings'], 
    #         icons=['house', '', 'gear'], menu_icon="cast", default_index=0)

    #     return selected

    # 2. horizontal menu
    # def body_menu(self):
    #     selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    #         icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #         menu_icon="cast", default_index=0, orientation="horizontal")
        
    #     return selected2
    @staticmethod
    def nav_menu():

        styles = {
        "container": {"margin": "0px !important", "padding": "0!important", "align-items": "stretch", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "lightblue", "font-size": "20px", "font-weight": "normal", "color": "black", },
        }

        styles1 = {
        "nav-link-selected": {"background-color": "#D1B000" },
        }

        menu = {
            'title' : 'Main Menu',
            'items': {
                'Home' : {
                    'action': None, 'item_icon': 'house', 'submenu': {
                        'title': None,
                        'items': {
                            'Home': {'action': home.home_page, 'item_icon': 'house', 'submenu': None },
                            'About Us': {'action': None, 'item_icon': 'people', 'submenu': None },
                            'Contact Us': {'action': None, 'item_icon': 'phone', 'submenu': None },
                        },
                        'menu_icon': 'cast',
                        'default_index': 0,
                        'with_view_panel': 'main',
                        'orientation': 'horizontal',
                        'styles': styles1
                    }
                },
                'AI Copilat' : {
                    'action': None, 'item_icon': 'chat', 'submenu': {
                        'title': None,
                        'items': {
                            'ChatBot': {'action': chat.chat, 'item_icon': 'robot', 'submenu': None },
                            'File Q&A': {'action': None, 'item_icon': 'cloud-upload', 'submenu': None },
                            'Text Summarizer': {'action': None, 'item_icon': 'list-task', 'submenu': None },
                            'Searching': {'action': None, 'item_icon': 'list-check', 'submenu': None }
                        },
                        'menu_icon': 'cast',
                        'default_index': 0,
                        'with_view_panel': 'main',
                        'orientation': 'horizontal',
                        'styles': styles1
                    }
                },
                'Settings' : {
                    'action': None, 'item_icon': 'gear', 'submenu': {
                        'title': None,
                        'items': {
                            'Home': {'action': None, 'item_icon': 'house', 'submenu': None },
                            'Upload': {'action': None, 'item_icon': 'cloud-upload', 'submenu': None },
                            'Task': {'action': None, 'item_icon': 'list-task', 'submenu': None },
                            'Manage Tasks': {'action': None, 'item_icon': 'list-check', 'submenu': None }
                        },
                        'menu_icon': None,
                        'default_index': 0,
                        'with_view_panel': 'main',
                        'orientation': 'horizontal',
                        'styles': styles1
                    }
                }
            },
            'menu_icon': 'clipboard2-check-fill',
            'default_index': 0,
            'with_view_panel': 'sidebar',
            'orientation': 'vertical',
            'styles': styles1
            }

        return menu

    @staticmethod
    def show_menu(menu):
        def _get_options(menu):
            options = list(menu['items'].keys())
            return options
        
        def _get_icons(menu):
            icons = [v['item_icon'] for _k, v in menu['items'].items()]
            return icons
        
        kwargs = {
        'menu_title': menu['title'] ,
        'options': _get_options(menu),
        'icons': _get_icons(menu),
        'menu_icon': menu['menu_icon'],
        'default_index': menu['default_index'],
        'orientation': menu['orientation'],
        'styles': menu['styles']
        }

        with_view_panel = menu['with_view_panel']
        if with_view_panel == 'sidebar':
            with st.sidebar: 
                menu_selection = option_menu(**kwargs)
        elif with_view_panel == 'main':
            menu_selection = option_menu(**kwargs)
        else:
            raise ValueError(f"Unknown view panel value: {with_view_panel}. Must be 'sidebar' or 'main'.")
        
        if menu['items'][menu_selection]['submenu']:
            Navigation.show_menu(menu['items'][menu_selection]['submenu'])

        if menu['items'][menu_selection]['action']:
            menu['items'][menu_selection]['action']()

