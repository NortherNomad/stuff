from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from database import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ID = None

class FSMadmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    # edit_photo = State()
    # edit_name = State()
    # edit_description = State()
    # edit_price = State()

# @dp.message_handler(commands=['модератор'], is_chat_admin=True)
async def make_change_command(message:types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что хозяин надо?', reply_markup=admin_kb.button_case_admin)
    await message.delete()

# '''Начало диалога загрузки нового пункта меню'''
# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMadmin.photo.set()
        await message.reply('Загрузи фото')

# '''Выход из состояний'''
# @dp.message_handler(state="*", commands='отмена')
# @dp.message_handler(Text(equals='отмена',ignore_case=True), state="*")
async def cancel_handler(message:types.Message, state=FSMContext):
    if message.from_user.id == ID:
        currentState = await state.get_state()
        if currentState is None:
            return
        await state.finish()
        await message.reply('Ok')

# '''Ловим первый ответ и пишем в словарь'''
# @dp.message_handler(content_types=['photo'], state=FSMadmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMadmin.next()
        await message.reply('Введите название кебаба')

async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMadmin.next()
        await message.reply('Введите описание')

# '''Ловим третий ответ'''
# @dp.message_handler(state=FSMadmin.description)
async def load_description(message:types.Message, state:FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMadmin.next()
        await message.reply('Введите цену')

# '''Ловим четвертый ответ'''
# @dp.message_handler(state=FSMadmin.price)
async def load_price(message:types.Message, state:FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        await sqlite_db.sql_add_command(state)
        await state.finish()

# @dp.message_handler(commands='Поменять позицию')
# async def change_position(message: types.Message):
#     if message.from_user.id == ID:
#         read = await sqlite_db.sql_read2()
#         if len(read) > 0:
#             for ret in read:
#                 await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
#                 await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Изменить {ret[1]}', callback_data=f'change {ret[1]}')))
#         else:
#             await bot.send_message(message.from_user.id, 'У вас пустое меню') 

# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('change '))
# async def change_data_item(callback: types.CallbackQuery, ):
#     if message.from_user.id == ID:
#         read = await sqlite_db.sql_read2()
#         if len(read) > 0:
#             for ret in read:
#                 await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
#                 await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))
#         else:
#             await bot.send_message(message.from_user.id, 'У вас пустое меню')


# @dp.message_handler(commands='Удалить')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        if len(read) > 0:
            for ret in read:
                await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
                await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))
        else:
            await bot.send_message(message.from_user.id, 'У вас пустое меню') 

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', '')) #{ret[1]}
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)

# async def edit_item(message: types.Message):
#     if message.from_user.id == ID:
#         read = await sqlite_db.sql_read2()
#         if len(read) > 0:
#             for ret in read:
#                 await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
#                 await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Изменить {ret[1]}', callback_data=f'edit {ret[1]}')))
#         else:
#             await bot.send_message(message.from_user.id, 'У вас пустое меню')                   

# # @dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))

# async def edit_callback_run(message:types.Message, callback_query: types.CallbackQuery, state=FSMContext):
#     async with state.proxy() as data:
#             data['name'] = message.text
#     await sqlite_db.sql_edit_title(callback_query.data.replace('edit ', ''), callback_query.data)


async def empty(message:types.Message):
    await message.answer('Нет такой команды')
    await message.delete()

#Регистрируем хэндлеры
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'])
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)    
    dp.register_message_handler(load_name, state=FSMadmin.name)
    dp.register_message_handler(load_description, state=FSMadmin.description)
    dp.register_message_handler(load_price, state=FSMadmin.price)
    dp.register_message_handler(make_change_command, commands=['модератор'], is_chat_admin=True)
    # dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '), is_chat_admin=True)
    # dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '), is_chat_admin=True)
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(delete_item, commands=['Удалить'])
    # dp.register_callback_query_handler(edit_callback_run, lambda x: x.data and x.data.startswith('edit '))
    # dp.register_message_handler(edit_item, commands=['Изменить_название'])
    dp.register_message_handler(empty)