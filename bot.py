import json
import telebot

import markups
import handle

# Create key.json file and provide a API key in it
with open('key.json') as f:
    key = json.load(f)
KEY = key['key']

# Authenticate bot
bot = telebot.TeleBot(KEY)


# Customize a start message
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     """Hi there! Choose an option below to check
bot's functionality.""",
                     reply_markup=markups.main_menu(),
                     )


# Handle text messages and button clicks from user.
@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    handle.user_messages(bot, message)


# Reply to a sticker message.
@bot.message_handler(content_types=["sticker"])
def get_file(message):
    text = f"Stciker ID: {message.sticker.file_id}"
    bot.send_message(message.chat.id,
                     text,
                     reply_markup=markups.main_menu(),
                     )


# Reply to a photo or image message.
@bot.message_handler(content_types=['photo', 'image'])
def send_photo(message):
    bot.send_chat_action(message.chat.id, 'upload_photo')
    img = open('bot.png', 'rb')
    bot.send_photo(message.chat.id, img,
                   reply_to_message_id=message.message_id)
    bot.send_message(message.chat.id,
                     "Here it is.",
                     reply_markup=markups.main_menu(),
                     )
    img.close()


bot.infinity_polling()
