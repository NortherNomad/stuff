from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove


button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')
# button_edit = KeyboardButton('/Изменить_название')


button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)