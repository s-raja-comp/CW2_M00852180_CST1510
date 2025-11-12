import bcrypt

password = 'Magic123'

def hash_password(password):
    binary_password = password.encode('utf-8') #b'Magic123'
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(binary_password, salt)
    return hashed.decode('utf-8')

password = 'Magic123'
hash = hash_password(password)

def validate_password (password, hash):
    psw = password.encode('utf-8')
    hash_ = hash.encode('utf-8')
    return bcrypt.checkpw(psw, hash_)

password = 'Magic123'
hash = hash_password(password)
print(hash)
print(validate_password(password,hash))

def register_user():
    user_name = input('Enter name: ')
    user_password = input('Enter password: ')
    hash = hash_password(user_password)
    with open('users.txt', 'a') as f:
        f.write(f'{user_name},{hash}\n')
    print ('User Registered!!')

def log_in():
    user_name = input('Enter name: ')
    user_password = input('Enter password: ')
    with open('users.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            name,hash = line.strip().split(',')
            if name == user_name:
                return validate_password(user_password, hash)
            return False
        
def menu():
    print('Welcome!!')
    print('Choose from the following options:')
    print('1. Register')
    print('2. Log in')
    print('3. Exit')

def main():
    while True:
        menu()
        choice = input (' > ')
        if choice == '1':
            register_user()
        elif choice == '2':
            log_in()
        elif choice == '3':
            print ('Goodbye!!')
            break