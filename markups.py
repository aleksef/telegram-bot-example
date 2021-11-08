from telebot import types


def blank():
    return types.ReplyKeyboardRemove()


def main_menu():
    main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Get Sticker ID")
    button2 = types.KeyboardButton("Images")
    main_menu.add(button1, button2)
    return main_menu
