import os
from utils import clear_terminal, exit_app, display_page_info

restaurants = [
    {
        'name': 'Pará Lanches',
        'type': 'Fast food',
        'status': True
    },
    {
        'name': 'Pizzaria do Cássio',
        'type': 'Pizzeria',
        'status': False
    }
]

def register_restaurant():
    display_page_info('REGISTER NEW RESTAURANT')

    restaurant_name = input('Enter restaurant name: ')
    restaurant_type = input('Enter restaurant type: ')
    print('\nLoading...\n')

    restaurant_data = {'name': restaurant_name, 'type': restaurant_type, 'status': False}
    restaurants.append(restaurant_data)

    print(f'{restaurant_name} has been registered successfully.\n')
    return_to_menu()

def list_restaurants():
    display_page_info('LIST OF ALL RESTAURANTS')
    list_all_restaurants()    
    return_to_menu()

def activate_restaurant():
    display_page_info('ACTIVATE RESTAURANT')
    list_all_restaurants()
    restaurant_name = input('Enter the name of the restaurant you want to activate/deactivate: ')
    print('\nLoading...\n')

    for restaurant in restaurants:
        if restaurant['name'].lower() == restaurant_name.lower():
            restaurant['status'] = not restaurant['status']
            
            if restaurant['status']:
                print(f'{restaurant_name} has been activated successfully.\n')
            else:
                print(f'{restaurant_name} has been deactivated successfully.\n')
            return_to_menu()

    print(f'{restaurant_name} was not found.\n')
    return_to_menu()

def display_menu():
    print('Food Delivey\n')

    print('1. Register restaurant')
    print('2. List restaurants')
    print('3. Activate/Deactivate restaurant')
    print('4. Exit')

    try:
        chosen_option = int(input('Type your option: '))
        match chosen_option:

            case 1:
                register_restaurant()

            case 2:
                list_restaurants()

            case 3:
                activate_restaurant()

            case 4:
                exit_app()

            case _:
                invalid_option()
    except:
        invalid_option()

def return_to_menu():
    input('\nPress any key to return to the menu')
    clear_terminal()
    display_menu()

def list_all_restaurants():
    for restaurant in restaurants:
        print(f'Name: {restaurant["name"].ljust(20)} | Type: {restaurant["type"].ljust(20)} | Status: {"Active" if restaurant["status"] else "Inactive"}')

def invalid_option():
    clear_terminal()
    print('Invalid option. Please try again.\n')
    display_menu()

def main():
    clear_terminal()
    display_menu()

if __name__ == '__main__':
    main()