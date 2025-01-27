import os
from utils import clear_terminal, invalid_option, exit_app, display_page_info, return_to_menu

restaurants = ['Pará Lanches', 'Pizzaria do Cássio']

def register_restaurant():
    display_page_info('REGISTER NEW RESTAURANT')
    restaurant_name = input('Enter restaurant name: ')
    restaurants.append(restaurant_name)
    print(f'{restaurant_name} has been registered successfully.\n')
    return_to_menu()

def list_restaurants():
    display_page_info('LIST OF ALL RESTAURANTS')
    for index, restaurant in enumerate(restaurants, start=1):
        print(f'{index}. {restaurant}\n')
    return_to_menu()

def display_menu():
    print('Food Delivey\n')

    print('1. Register restaurant')
    print('2. List restaurants')
    print('3. Activate restaurant')
    print('4. Exit')

    try:
        chosen_option = int(input('Type your option: '))
        match chosen_option:

            case 1:
                register_restaurant()

            case 2:
                list_restaurants()

            case 3:
                print('Activating restaurant...')

            case 4:
                exit_app()

            case _:
                invalid_option()
    except:
        invalid_option()

def main():
    clear_terminal()
    display_menu()

if __name__ == '__main__':
    main()