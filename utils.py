import os
from main import display_menu

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def invalid_option():
    clear_terminal()
    print('Invalid option. Please try again.')
    display_menu()

def exit_app():
    clear_terminal()
    print('Food Delivery app is closing...\n')

def display_page_info(page_name):
    clear_terminal()
    print(f'{page_name}\n')

def return_to_menu():
    input('Press any key to return to the menu')
    clear_terminal()
    display_menu()