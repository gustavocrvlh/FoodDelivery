import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_app():
    print('Food Delivery app is closing...')
    clear_terminal()
    print('Food Delivery app is closed.\n')

def display_page_info(page_name):
    clear_terminal()
    print(f'{page_name}\n')

