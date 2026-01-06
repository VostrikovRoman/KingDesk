import telebot, webbrowser
from telebot import types
from random import randint
import requests
import os


bot = telebot.TeleBot('7880658577:AAGwp2PVm1pgEPuMGRxH9K_8DQAOjgApYSw')
division = ''

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', 'https://kingdesk.ru'))
    markup.add(types.InlineKeyboardButton('Отправить расписание', callback_data='import_from_excel')),
    markup.add(types.InlineKeyboardButton('Получить расписание', callback_data='export_to_excel')),
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}.\n\nМеня зовут Паша. Я помогу тебе в работе с сайтом KING_Desk.")
    bot.send_message(message.chat.id, "Ниже ты можешь увидеть функции, с помощью которых ты сможешь взаимодействовать с сайтом", reply_markup=markup)

# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'random':
#         r = randint(0,255)
#         g = randint(0,255)
#         b = randint(0,255)
#         color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
#         markup = types.InlineKeyboardMarkup()
#         markup.add(types.InlineKeyboardButton('Перейти на сайт', 'https://get-color.ru/' + color))
#         bot.send_message(callback.message.chat.id, f'Ваш рандомный цвет: {color}', reply_markup=markup)

@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        if message.document.file_name[-5:] == '.xlsx':
            src = 'home/frosty/kingdesk_dir/downloads/Raspisanie_580.xlsx'
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, "Ваш файл отправлен на сайт")
        else:
            bot.reply_to(message, 'Неверный формат! Попробуйте отправить снова')
    except Exception as e:
        bot.reply_to(message, 'Произошла какая-то ошибка! Попробуйте позже')  

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'import_from_excel':
        bot.send_message(callback.message.chat.id, 'Хорошо. Тебе нужно отправить файл в формате ".xlsx"') 
    if callback.data == 'export_to_excel':
        try:
            chat_id = callback.message.chat.id

            src = 'home/frosty/kingdesk_dir/downloads/Raspisanie_580.xlsx'
            if os.path.exists(src):
                bot.send_message(callback.message.chat.id, 'Конечно, держи!')
                with open(src, 'rb') as new_file:
                    bot.send_document(chat_id=chat_id, document=new_file)
            else:
                bot.send_message(callback.message.chat.id, 'Произошла какая-то ошибка! Попробуйте позже')
                
        except Exception as e:
            bot.send_message(callback.message.chat.id, 'Произошла какая-то ошибка! Попробуйте позже')
          

@bot.message_handler(commands=['import'])
def import_doc(message):
    try:
        chat_id = message.chat.id

        src = 'home/frosty/kingdesk_dir/downloads/Raspisanie_580.xlsx'
        if os.path.exists(src):
            bot.send_message(chat_id, 'Конечно, держи!')
            with open(src, 'rb') as new_file:
                bot.send_document(chat_id=chat_id, document=new_file)
        else:
            bot.send_message(chat_id, 'Произошла какая-то ошибка! Попробуйте позже')
                
    except Exception as e:
        bot.send_message(message.chat.id, 'Произошла какая-то ошибка! Попробуйте позже')

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://kingdesk.ru')

bot.polling(non_stop=True)