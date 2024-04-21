import telebot
import datetime
import holidays

bot = telebot.TeleBot('7180407632:AAGCgvAeiKh-vSSAxBb0KJtvRGULlR5P4ts')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет\n'
                                      'я могу показать какой сегодня праздник\n'
                                      'напиши команду /holiday')

@bot.message_handler(commands=['holiday'])
def holiday(message):
    today = datetime.date.today()
    current_year = today.year
    current_mounth = today.month
    current_day = today.day

    holiday_list = holidays.Russia(year = current_year)

    if today in holiday_list:
        bot.send_message(message.chat.id, f'сегодня праздник {holiday_list[today]}')
    else:
        bot.send_message(message.chat.id, f'сегодня нет никаких праздников')

bot.polling(none_stop=True, interval=0)