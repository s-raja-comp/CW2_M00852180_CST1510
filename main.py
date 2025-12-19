import bcrypt
import sqlite3

def generate_hash(password):
    binary_password = password.encode('utf-8') #b'Magic123'
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(binary_password, salt)
    return hash.decode('utf-8')

def validate_password (password, hash):
    binary_password = password.encode('utf-8')
    hash_ = hash.encode('utf-8')
    is_valid = bcrypt.checkpw(binary_password, hash_)
    return is_valid

password = 'Magic123'

# registering a user #3
def register_user():
    user_name = input('Enter name: ')
    user_password = input('Enter password: ')
    hash_password = generate_hash(password)
    with open('DATA/users.txt', 'a') as f:
        f.write(f'{user_name},{hash_password}\n')
    print ('User Registered!!')

# log in user #
def log_in():
    user_name = input('Enter name: ')
    user_password = input('Enter password: ')
    with open('DATA/users.txt', 'r') as f:
        users = f.readlines()
    for user in users:
        user_name,user_password = user.strip().split(',')
        if user_name == user_name and validate_password(user_password, hash):
             return True
    return False

def menu():
    print('Welcome!!')
    print('Choose from the following options:')
    print('1. Register')
    print('2. Log in')
    print('3. Exit')

def main():
    flag = True
    while flag:
        menu()
        choice = input (' > ')

        match choice:
            case "1":
                register_user()
            case "2":
                if log_in():
                    print('Logged in successfully!')
                else:
                    print('Incorrect. Try again.')
            case '3':
                print ('Goodbye!!')
                flag = False
            case _:
                print("Incorrect input!")
main()

conn = sqlite3.connect('DATA/intelligence_platform.db')
curr = conn.cursor
sql = '''CREATE TABLE users ( 
id INTEGER PRIMARY KEY AUTOINCREMENT, 
username TEXT NOT NULL UNIQUE, 
password_hash TEXT NOT NULL); 
'''
curr.execute(sql)
conn.commit()
conn.close()

def add_user(conn, name, hash):
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    curr = conn.cursor
    sql = '''INSERT INTO users (username, password_hash) VALUES (?, ?) '''
    param = (name, hash)
    curr.execute(sql, param)
    conn.commit()
conn.close()