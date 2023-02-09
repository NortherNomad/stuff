from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from database import sqlite_db

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Бот готов к работе', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/OOPKanyshBot')

@dp.message_handler(commands=['Режим_работы'])
async def work_schedule(message : types.Message):
    await bot.send_message(message.from_user.id, '**Вс-Чт** 09:00-18:00, **Пт-Сб** 10:00-19:00')

@dp.message_handler(commands=['Геопозиция'])
async def work_place(message : types.Message):
    await bot.send_message(message.from_user.id, 'Орбита-4, дом 27')

# @dp.message_handler(commands=['Меню'])
async def kebab_menu_command(message:types.Message):
    await sqlite_db.sql_read(message)

# async def order(message: types.Message):
#     read = await sqlite_db.sql_read2()
#     if len(read)>0:
#         for ret in read:    
#             await bot.send_message(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
#             await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Заказать {ret[1]}', callback_data=f'order {ret[1]}')))
#     else:
#         await bot.send_message(message.from_user.id, 'В меню временно нет позиций, просим прощения :(')

# # @dp.callback_query_handler(lambda x: x.data and x.data.startswith('order '))
# async def order_callback_run(callback_query: types.CallbackQuery):
#     await sqlite_db.sql_delete_command(callback_query.data.replace('order ', ''))
#     await callback_query.answer(text='Ваш заказ принят', show_alert=True)

#Регистрируем хэндлеры
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(work_schedule, commands=['Режим_работы'])    
    dp.register_message_handler(work_place, commands=['Геопозиция'])
    dp.register_message_handler(kebab_menu_command, commands=['Меню'])
    # dp.register_callback_query_handler(order_callback_run, lambda x: x.data and x.data.startswith('order '))
    # dp.register_message_handler(order, commands=['Заказать'])






















    