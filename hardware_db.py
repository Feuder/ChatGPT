        print(
            "\nOptions: register, login, add_group, add_person, "
            "add_hardware, list, quit"
        )
    register_user,
    login_user,
    add_group,
    add_person,
    add_hardware,
    list_hardware,
)
=======
import sqlite3
import hashlib

DB_NAME = 'hardware.db'

# Initialize database with tables if not exist
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS hardware (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_id INTEGER,
    person_id INTEGER,
    FOREIGN KEY(group_id) REFERENCES groups(id),
    FOREIGN KEY(person_id) REFERENCES persons(id)
)''')

conn.commit()
conn.close()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username: str, password: str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)',
                    (username, hash_password(password)))
        conn.commit()
        print('User registered successfully.')
    except sqlite3.IntegrityError:
        print('Username already exists.')
    finally:
        conn.close()

def login(username: str, password: str) -> bool:
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('SELECT password_hash FROM users WHERE username=?', (username,))
    row = cur.fetchone()
    conn.close()
    if row and row[0] == hash_password(password):
        return True
    return False

def add_group(name: str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO groups (name) VALUES (?)', (name,))
        conn.commit()
        print('Group added.')
    except sqlite3.IntegrityError:
        print('Group already exists.')
    finally:
        conn.close()

def add_person(name: str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO persons (name) VALUES (?)', (name,))
        conn.commit()
        print('Person added.')
    except sqlite3.IntegrityError:
        print('Person already exists.')
    finally:
        conn.close()

def add_hardware(name: str, group_id=None, person_id=None):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('INSERT INTO hardware (name, group_id, person_id) VALUES (?, ?, ?)',
                (name, group_id, person_id))
    conn.commit()
    conn.close()
    print('Hardware added.')

def list_hardware():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''SELECT hardware.id, hardware.name, groups.name, persons.name
                   FROM hardware
                   LEFT JOIN groups ON hardware.group_id = groups.id
                   LEFT JOIN persons ON hardware.person_id = persons.id''')
    rows = cur.fetchall()
    conn.close()
    print('\nHardware Items:')
    for row in rows:
        hw_id, hw_name, group_name, person_name = row
        print(f'ID: {hw_id}, Name: {hw_name}, Group: {group_name}, Person: {person_name}')
 main


def main():
    print('Hardware Database CLI')
    while True:
        print('\nOptions: register, login, add_group, add_person, add_hardware, list, quit')
        option = input('Select option: ').strip()
        if option == 'register':
            username = input('Username: ')
            password = input('Password: ')
 dwnpad-codex/datenbank-für-hardware-mit-auth-erstellen
            if register_user(username, password):
                print('User registered successfully.')
            else:
                print('Username already exists.')
        elif option == 'login':
            username = input('Username: ')
            password = input('Password: ')
            if login_user(username, password):
=======
            register_user(username, password)
        elif option == 'login':
            username = input('Username: ')
            password = input('Password: ')
            if login(username, password):
 main
                print('Login successful.')
            else:
                print('Login failed.')
        elif option == 'add_group':
            name = input('Group name: ')
 dwnpad-codex/datenbank-für-hardware-mit-auth-erstellen
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
=======
            add_group(name)
        elif option == 'add_person':
            name = input('Person name: ')
            add_person(name)
 main
        elif option == 'add_hardware':
            name = input('Hardware name: ')
            group_id = input('Group ID (optional): ')
            person_id = input('Person ID (optional): ')
            group_id = int(group_id) if group_id else None
            person_id = int(person_id) if person_id else None
            add_hardware(name, group_id, person_id)
 dwnpad-codex/datenbank-für-hardware-mit-auth-erstellen
            print('Hardware added.')
        elif option == 'list':
            rows = list_hardware()
            print('\nHardware Items:')
            for row in rows:
                hw_id, hw_name, group_name, person_name = row
                print(
                    f'ID: {hw_id}, Name: {hw_name}, Group: {group_name}, Person: {person_name}'
                )
=======
        elif option == 'list':
            list_hardware()
 main
        elif option == 'quit':
            break
        else:
            print('Unknown option.')

 dwnpad-codex/datenbank-für-hardware-mit-auth-erstellen

=======
 main
if __name__ == '__main__':
    main()
