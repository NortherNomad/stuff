import sqlite3 as sq
from create_bot import bot
from datetime import datetime
time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")

def sql_start():
    global base, cur
    base = sq.connect('kebab_cool.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    # base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

# async def sql_change_command(state):
#     async with state.proxy() as data:
#         cur.execute('UPDATE menu SET ')

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES(?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    if len(cur.execute('SELECT * FROM menu').fetchall()) > 0:
        for ret in cur.execute('SELECT * FROM menu').fetchall():
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')
    else:
        await bot.send_message(message.from_user.id, 'В меню временно нет позиций, просим прощения :(')


async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name ==?', (data,))
    base.commit()

async def sql_order_command(data):
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    cur.execute('INSERT INTO menu (order_name, time)', (data, time_now,))
    base.commit()

# async def sql_edit_title(data):
#     cur.execute('UPDATE menu SET name = ? WHERE price == ?', (data['name'],data['price'],))
#     base.commit()

# async def sql_edit_title(data):
#     cur.execute('UPDATE menu SET name = "" WHERE name == ?', (data,))
#     base.commit()