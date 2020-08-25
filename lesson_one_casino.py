import sqlite3
from random import randint

global db
global sql

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash INT
)""")

db.commit()

def reg():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM users WHERE login ='{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_password, 0))
        db.commit()

        print("Registered!")
    else:
        print("Entry already exists!")

        for value in sql.execute("SELECT * FROM users"):
            print(value)

def delete_db():
    sql.execute(f"DELETE FROM users WHERE login = '{user_login}'")
    db.commit()

    print('Entry deleted!')

def casino():
    global user_login
    user_login = input('Log in: ')
    user_password = input('Password: ')
    number = randint(1,2)

    for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
        balance = i[0]

    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    sql.execute(f'SELECT password FROM users WHERE password = "{user_password}"')
    if sql.fetchone() is None:
        print("Login does not exist or Wrong password. Please register!")
        reg()
    else:
       if number == 1:
            sql.execute(f'UPDATE users SET cash = {1000 + balance} WHERE login = "{user_login}"')
            db.commit()
       else:
        print('You Lose!')
        delete_db()






def enter():
   # for i in sql.execute('SELECT login, cash FROM users'):
   #     print(i)
   sql.execute('SELECT login, cash From users')
   row = sql.fetchall()
   print(row)

def main():
    casino()
    enter()

main()
