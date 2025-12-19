import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(stored_password: str, provided_password: str) -> bool:
 ### Verify a stored password against one provided by user ###
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

def set_user(conn, name, hash):
    curr = conn.cursor()
    sql = ' ' ###INSERT INTO users (user_name, password_hash) VALUES (?,?)###
    param = (name, hash)
    curr.execute(sql, param)
    conn.commit()

def get_one_user(conn, name):
    curr = conn.cursor()
    sql = ' ' ###SELECT * FROM users WHERE user_name = ?###
    param = (name,)
    curr.execute(sql, param)
    user = curr.fetchone()
    return(user)

def user_registration(conn):
    name = input("Enter your name to register: ")
    password = input ("Enter a password to register: ")
    hash = hash_password(password)