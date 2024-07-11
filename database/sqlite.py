import sqlite3
from datetime import datetime
#from aiogram import types

base =sqlite3.connect('nail0s.db')
cursor =base.cursor()
base.autocommit = True

def sql_start():
    if base:
        cursor.execute('CREATE TABLE IF NOT EXISTS users('
                   'date DATETIME,'
                   'id_tg INTEGER PRIMARY KEY, '
                   'client_username TEXT,'
                   'inst TEXT, '
                   'phone_num TEXT, '
                   'register INTEGER)')

        cursor.execute('CREATE TABLE IF NOT EXISTS enroll('
                       'created_date DATETIME, '
                       'admin_id_tg INTEGER, '
                       'place TEXT'
                       'session_date DATETIME, '
                       'id_tg_client INTEGER)')


def sql_add_user(id_tg, username):
    sql_query = f'INSERT INTO users (date, id_tg, client_username, inst, phone_num, register) VALUES (?, ?, ?, ?, ?, ?)'

    cursor.execute(sql_query, (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),) + (id_tg, username, 0, 0, 0, ))


def sql_check_reg(id: int):
    res = cursor.execute(f'SELECT register FROM users WHERE id_tg = {id}').fetchone()
    print(res)
    if res == None or res[0] == 0:
        return 0
    return 1


def sql_update_inst(id: int, inst: str):
    cursor.execute('UPDATE users SET inst = ? WHERE id_tg = ?', (inst, id))

def sql_update_phone(id, phone):# изменение телефона
    cursor.execute('UPDATE users SET phone_num = ? WHERE id_tg = ?', (phone, id))

def sql_update_register(id, register: bool):
    cursor.execute("UPDATE users SET register = ? WHERE id_tg = ?", (register, id))