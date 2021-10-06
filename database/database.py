import sqlite3

URL_DATABASE = 'databese/Banco.db'

def connect_db():
    conn = sqlite3.connect(URL_DATABASE)
    return conn