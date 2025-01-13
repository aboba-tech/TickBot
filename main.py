import asyncio
import logging
import sys
import time
import db

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram import types

TOKEN = '7858809144:AAEKo_A_03_-qeRa4b1l19sBoJNuFWSV3WY'
default = DefaultBotProperties(parse_mode='HTML')

dp = Dispatcher()
bot = Bot(token=TOKEN, default=default)

# клавиатура
button_bz = types.InlineKeyboardButton(text='Засчитать бзик', callback_data='count_bz')
button_bz_remove = types.InlineKeyboardButton(text='Убрать бзик', callback_data='remove_bz')
button_pr = types.InlineKeyboardButton(text='Засчитать приступ', callback_data='count_pr')
button_pr_remove = types.InlineKeyboardButton(text='Убрать приступ', callback_data='remove_pr')
button_data = types.InlineKeyboardButton(text='Посмотреть подробную статистику', callback_data='all_data')
buttons = [[button_bz, button_pr], [button_bz_remove, button_pr_remove]]
aboba_keys = types.InlineKeyboardMarkup(inline_keyboard=buttons)


@dp.message(CommandStart())
async def start(message: types.Message):

    checker = db.check_user(message.chat.id)
    if checker:
        print('user already exists')

    data = db.view_all_data_full(message.chat.id)
    bz = sum(data[1:8])
    pr = sum(data[-7:-1])

    await bot.send_message(chat_id=message.chat.id,
                    text=f"Привет! Этот бот подсчитывает приступы. Твои данные будут показываться тут.\n"
                        f"<b>Общее количество приступов:</b>{pr}\n"
                        f"<b>Общее количество бзиков:</b>{bz}", 
                    reply_markup=aboba_keys)
    
    

    
@dp.callback_query()
async def handler(callback_query: types.CallbackQuery):


    # клавиатура колбэков бзиков
    bz_2 = types.InlineKeyboardButton(text=f'бзик 2', callback_data='count_bz2')
    bz_3 = types.InlineKeyboardButton(text=f'бзик 3', callback_data='count_bz3')
    bz_1 = types.InlineKeyboardButton(text=f'бзик 1', callback_data='count_bz1')
    bz_4 = types.InlineKeyboardButton(text=f'бзик 4', callback_data='count_bz4')
    bz_5 = types.InlineKeyboardButton(text=f'бзик 5', callback_data='count_bz5')
    bz_6 = types.InlineKeyboardButton(text=f'бзик 6', callback_data='count_bz6')
    bz_7 = types.InlineKeyboardButton(text=f'бзик 7', callback_data='count_bz7')
    back = types.InlineKeyboardButton(text=f'Назад', callback_data='back')
    local_buttons = [[bz_1, bz_2, bz_3], [bz_4, bz_5, bz_6], [bz_7], [back]]
    keyboard_bz = types.InlineKeyboardMarkup(inline_keyboard=local_buttons)

    # клавиатура колбэков удаления бзиков
    bz_2 = types.InlineKeyboardButton(text=f'бзик 2', callback_data='remove_bz2')
    bz_3 = types.InlineKeyboardButton(text=f'бзик 3', callback_data='remove_bz3')
    bz_1 = types.InlineKeyboardButton(text=f'бзик 1', callback_data='remove_bz1')
    bz_4 = types.InlineKeyboardButton(text=f'бзик 4', callback_data='remove_bz4')
    bz_5 = types.InlineKeyboardButton(text=f'бзик 5', callback_data='remove_bz5')
    bz_6 = types.InlineKeyboardButton(text=f'бзик 6', callback_data='remove_bz6')
    bz_7 = types.InlineKeyboardButton(text=f'бзик 7', callback_data='remove_bz7')
    back = types.InlineKeyboardButton(text=f'Назад', callback_data='back')
    local_buttons = [[bz_1, bz_2, bz_3], [bz_4, bz_5, bz_6], [bz_7], [back]]
    keyboard_remove_bz = types.InlineKeyboardMarkup(inline_keyboard=local_buttons)

    # клавиатура колбэков приступов
    bz_2 = types.InlineKeyboardButton(text=f'приступ 2', callback_data='count_pr2')
    bz_3 = types.InlineKeyboardButton(text=f'приступ 3', callback_data='count_pr3')
    bz_1 = types.InlineKeyboardButton(text=f'приступ 1', callback_data='count_pr1')
    bz_4 = types.InlineKeyboardButton(text=f'приступ 4', callback_data='count_pr4')
    bz_5 = types.InlineKeyboardButton(text=f'приступ 5', callback_data='count_pr5')
    bz_6 = types.InlineKeyboardButton(text=f'приступ 6', callback_data='count_pr6')
    bz_7 = types.InlineKeyboardButton(text=f'приступ 7', callback_data='count_pr7')
    back = types.InlineKeyboardButton(text=f'Назад', callback_data='back')
    local_buttons = [[bz_1, bz_2, bz_3], [bz_4, bz_5, bz_6], [bz_7], [back]]
    keyboard_pr = types.InlineKeyboardMarkup(inline_keyboard=local_buttons)

    # клавиатура колбэков удаления приступов
    bz_2 = types.InlineKeyboardButton(text=f'приступ 2', callback_data='remove_pr2')
    bz_3 = types.InlineKeyboardButton(text=f'приступ 3', callback_data='remove_pr3')
    bz_1 = types.InlineKeyboardButton(text=f'приступ 1', callback_data='remove_pr1')
    bz_4 = types.InlineKeyboardButton(text=f'приступ 4', callback_data='remove_pr4')
    bz_5 = types.InlineKeyboardButton(text=f'приступ 5', callback_data='remove_pr5')
    bz_6 = types.InlineKeyboardButton(text=f'приступ 6', callback_data='remove_pr6')
    bz_7 = types.InlineKeyboardButton(text=f'приступ 7', callback_data='remove_pr7')
    back = types.InlineKeyboardButton(text=f'Назад', callback_data='back')
    local_buttons = [[bz_1, bz_2, bz_3], [bz_4, bz_5, bz_6], [bz_7], [back]]
    keyboard_remove_pr = types.InlineKeyboardMarkup(inline_keyboard=local_buttons)


    if callback_query.data == 'count_bz':
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id, text="Выбери степень бзика", reply_markup=keyboard_bz)


    if callback_query.data == 'count_bz1':
        data = db.add_bz(callback_query.message.chat.id, 1, '1')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_bz)


    if callback_query.data == 'count_bz2':
        data = db.add_bz(callback_query.message.chat.id, 1, '2')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_bz)


    if callback_query.data == 'count_bz3':
        data = db.add_bz(callback_query.message.chat.id, 1, '3')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_bz)


    if callback_query.data == 'count_bz4':
        data = db.add_bz(callback_query.message.chat.id, 1, '4')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_bz)


    if callback_query.data == 'count_bz5':
        data = db.add_bz(callback_query.message.chat.id, 1, '5')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_bz)


    if callback_query.data == 'count_bz6':
        data = db.add_bz(callback_query.message.chat.id, 1, '6')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_bz)


    if callback_query.data == 'count_bz7':
        data = db.add_bz(callback_query.message.chat.id, 1, '7')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_bz)



    










        # db.add_bz(callback_query.message.chat.id, 1)
        # data = db.view_all_data(callback_query.message.chat.id)
        # bz = data[0]
        # pr = data[1]
        # await bot.edit_message_text(text=f"Привет! Этот бот подсчитывает приступы. Твои данные будут показываться тут.\n"
        # f"<b>Общее количество приступов:</b>{pr}\n"
        # f"<b>Общее количество бзиков:</b>{bz}", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        # reply_markup=aboba_keys)


    if callback_query.data == 'remove_bz':
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id, text="Выбери степень бзика", reply_markup=keyboard_remove_bz)

        
    if callback_query.data == 'remove_bz1':
        data = db.remove_bz(callback_query.message.chat.id, 1, '1')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_bz)


    if callback_query.data == 'remove_bz2':
        data = db.remove_bz(callback_query.message.chat.id, 1, '2')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_bz)


    if callback_query.data == 'remove_bz3':
        data = db.remove_bz(callback_query.message.chat.id, 1, '3')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_bz)


    if callback_query.data == 'remove_bz4':
        data = db.remove_bz(callback_query.message.chat.id, 1, '4')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_bz)


    if callback_query.data == 'remove_bz5':
        data = db.remove_bz(callback_query.message.chat.id, 1, '5')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_bz)

    if callback_query.data == 'remove_bz6':
        data = db.remove_bz(callback_query.message.chat.id, 1, '6')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_bz)


    if callback_query.data == 'remove_bz7':
        data = db.remove_bz(callback_query.message.chat.id, 1, '7')
        bz1, bz2, bz3, bz4, bz5, bz6, bz7 = data[1], data[2], data[3], data[4], data[5], data[6], data[7]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество бзиков:</b>{sum(data[1:8])}\n"
        f"<b>Бзики 1: </b>{bz1}\n<b>Бзики 2: </b>{bz2}\n<b>Бзики 3: </b>{bz3}\n"
        f"<b>Бзики 4: </b>{bz4}\n<b>Бзики 5: </b>{bz5}\n<b>Бзики 6: </b>{bz6}\n"
        f"<b>Бзики 7: </b>{bz7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_bz)

    
    if callback_query.data == 'count_pr':
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id, text="Выбери степень приступа", reply_markup=keyboard_pr)


    if callback_query.data == 'count_pr1':
        data = db.add_pr(callback_query.message.chat.id, 1, '1')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_pr)


    if callback_query.data == 'count_pr2':
        data = db.add_pr(callback_query.message.chat.id, 1, '2')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_pr)


    if callback_query.data == 'count_pr3':
        data = db.add_pr(callback_query.message.chat.id, 1, '3')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_pr)

    if callback_query.data == 'count_pr4':
        data = db.add_pr(callback_query.message.chat.id, 1, '4')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_pr)


    if callback_query.data == 'count_pr5':
        data = db.add_pr(callback_query.message.chat.id, 1, '5')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_pr)


    if callback_query.data == 'count_pr6':
        data = db.add_pr(callback_query.message.chat.id, 1, '6')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_pr)


    if callback_query.data == 'count_pr7':
        data = db.add_pr(callback_query.message.chat.id, 1, '7')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_pr)
 

    if callback_query.data == 'remove_pr1':
        data = db.remove_pr(callback_query.message.chat.id, 1, '1')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_pr)


    if callback_query.data == 'remove_pr2':
        data = db.remove_pr(callback_query.message.chat.id, 1, '2')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_pr)


    if callback_query.data == 'remove_pr3':
        data = db.remove_pr(callback_query.message.chat.id, 1, '3')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_pr)
    
          
    if callback_query.data == 'remove_pr4':
        data = db.remove_pr(callback_query.message.chat.id, 1, '4')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_pr)


    if callback_query.data == 'remove_pr5':
        data = db.remove_pr(callback_query.message.chat.id, 1, '5')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_pr)


    if callback_query.data == 'remove_pr6':
        data = db.remove_pr(callback_query.message.chat.id, 1, '6')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_pr)


    if callback_query.data == 'remove_pr7':
        data = db.remove_pr(callback_query.message.chat.id, 1, '7')
        pr1, pr2, pr3, pr4, pr5, pr6, pr7 = data[-7], data[-6], data[-5], data[-4], data[-3], data[-2], data[-1]
        await bot.edit_message_text(text=f"Твои данные будут показываться тут.\n"
        f"<b>Общее количество приступов:</b>{sum(data[-7:-1])}\n"
        f"<b>Приступ 1: </b>{pr1}\n<b>Приступ 2: </b>{pr2}\n<b>Приступ 3: </b>{pr3}\n"
        f"<b>Приступ 4: </b>{pr4}\n<b>Приступ 5: </b>{pr5}\n<b>Приступ 6: </b>{pr6}\n"
        f"<b>Приступ 7: </b>{pr7}\n", chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        reply_markup=keyboard_remove_pr)


    if callback_query.data == 'remove_pr':
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id, text="Выбери степень приступа", reply_markup=keyboard_remove_pr)
    




    if callback_query.data == 'back':
        data = db.view_all_data_full(callback_query.message.chat.id)
        bz = sum(data[1:8])
        pr = sum(data[-7:-1])

        await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                    text=f"Привет! Этот бот подсчитывает приступы. Твои данные будут показываться тут.\n"
                        f"<b>Общее количество приступов:</b>{pr}\n"
                        f"<b>Общее количество бзиков:</b>{bz}", 
                    reply_markup=aboba_keys)



    
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

