from database import (
    register_user,
    login_user,
    add_group,
    add_person,
    add_hardware,
    list_hardware,
)


def main():
    print('Hardware Database CLI')
    while True:
        print(
            "\nOptions: register, login, add_group, add_person, "
            "add_hardware, list, quit"
        )
        option = input('Select option: ').strip()
        if option == 'register':
            username = input('Username: ')
            password = input('Password: ')
            if register_user(username, password):
                print('User registered successfully.')
            else:
                print('Username already exists.')
        elif option == 'login':
            username = input('Username: ')
            password = input('Password: ')
            if login_user(username, password):
                print('Login successful.')
            else:
                print('Login failed.')
        elif option == 'add_group':
            name = input('Group name: ')
            if add_group(name):
                print('Group added.')
            else:
                print('Group already exists.')
        elif option == 'add_person':
            name = input('Person name: ')
            if add_person(name):
                print('Person added.')
            else:
                print('Person already exists.')
        elif option == 'add_hardware':
            name = input('Hardware name: ')
            group_id = input('Group ID (optional): ')
            person_id = input('Person ID (optional): ')
            group_id = int(group_id) if group_id else None
            person_id = int(person_id) if person_id else None
            add_hardware(name, group_id, person_id)
            print('Hardware added.')
        elif option == 'list':
            rows = list_hardware()
            print('\nHardware Items:')
            for row in rows:
                hw_id, hw_name, group_name, person_name = row
                print(
                    f'ID: {hw_id}, Name: {hw_name}, Group: {group_name}, Person: {person_name}'
                )
        elif option == 'quit':
            break
        else:
            print('Unknown option.')

if __name__ == '__main__':
    main()
