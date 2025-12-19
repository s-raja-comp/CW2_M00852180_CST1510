import sqlite3
import pandas as pd


def create_user_table(conn):
    curr = conn.cursor()
    sql = ("""CREATE TABLE IF NOT EXISTS users ( 
           id INTEGER PRIMARY KEY AUTOINCREMENT, 
           username TEXT NOT NULL UNIQUE, 
           password_hash TEXT NOT NULL
           )  """)
    curr.execute(sql)
    conn.commit()

def add_user(conn, name, hash):
    curr = conn.cursor()
    sql = """ INSERT INTO users (username, password_hash) VALUES (?, ?)"""
    param = (name, hash)
    curr.execute(sql, param)
    conn.commit()

def get_all_users(conn):
    curr = conn.cursor()
    sql = """SELECT * FROM users"""
    curr.execute(sql)
    users = curr.fetchall()
    conn.close()
    return(users)

# Migration functions

def migrate_users(conn):
    with open('DATA\users.txt','r') as f:
        users = f.readlines()

    for user in users:
        name, hash = user.strip().split(',')
        print(name, hash)
        add_user(conn, name, hash)

#conn.close()

def migrate_cyber_incidents(conn):
    data1 = pd.read_csv("DATA\\cyber_incidents.csv")
    data1.to_sql('cyber_incidents', conn, if_exists='append', index=False) 
    print ('Data load')

def get_all_users_pandas():
# Creating a database connection
    conn = sqlite3.connect("DATA\\intelligence_platform.db")

# Execute SQL query and load result into Dataframe
    query = "SELECT * FROM users"
    df = pd.read_sql(query,conn)
    return (df)

def migrate_it_tickets(conn):
    data1 = pd.read_csv('C:\VSCodeProjects\CW2_M00852180_CST1510\CW2_M00852180_CST1510\DATA\it_tickets.csv')
    data1.to_sql('cyber_incidents', conn, if_exists='append', index=False)
    print ('Data load')