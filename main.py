import telebot

bot = telebot.TeleBot('6671873953:AAG7oKuVPyqCdywNfN0P-lcHxFrEhIDe-PI')

@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)

    bot.send_message(message.from_user.id, f'{message.from_user.first_name} Hello')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.from_user.id, f'{message.from_user.first_name} Done!')




bot.infinity_polling()