import markups


sti = "CAACAgIAAxkBAAP8YYk5ti1OTRhH9xKhO3YeZwABp7swAAIUEAACRd7YS4GzdytDqYx1IgQ"


def user_messages(bot, message):
    if message.text == "Get Sticker ID":
        text = "Send me a sticker and I'll tell you it's ID."
        bot.send_message(message.chat.id,
                         text,
                         reply_markup=markups.blank(),
                         )
        return
    if message.text == "Images":
        bot.send_message(message.chat.id,
                         "Send me your image and I'll send you mine.",
                         reply_markup=markups.blank(),
                         )
        return
    else:
        bot.send_message(message.chat.id,
                         "Sorry, I don't understand your request."),
        bot.send_sticker(message.chat.id, sti,
                         reply_markup=markups.main_menu(),)
        return
