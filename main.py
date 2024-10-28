import requests
import telebot
from telebot import types

from config import token_tg

bot = telebot.TeleBot(token_tg)


@bot.message_handler(commands=['start'])
def start_message(message):
    # Create markup for the button
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    get_bitcoin_price_but = types.KeyboardButton('Get Bitcoin Price')
    markup.add(get_bitcoin_price_but)

    # Send a welcome message and create the button
    bot.send_message(message.chat.id, f'<b>Hi, {message.from_user.first_name}!</b>\n', parse_mode='html')
    bot.send_message(message.chat.id, 'Click the button to get the current price of Bitcoin.', reply_markup=markup)


@bot.message_handler()
def get_bitcoin_price(message):
    # Get Bitcoin price
    if message.text.lower() == 'get bitcoin price':
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

        # Setting up the bot's response
        date_and_time = response.json()['time']['updated']
        parts_of_date_and_time = date_and_time.split()
        date_part = ' '.join(parts_of_date_and_time[:3])
        time_part = ' '.join(parts_of_date_and_time[3:])
        price = response.json()['bpi']['USD']['rate_float']
        formatted_price = "{:,.2f}".format(price)

        # Send the date, time, and Bitcoin price
        bot.send_message(message.chat.id, f'Date: {date_part}\n'
                                          f'Time: {time_part}\n'
                                          f'<b>Price: ${formatted_price}</b>', parse_mode='html')

    # Unrecognized command
    else:
        bot.send_message(message.chat.id, 'Oops... Unrecognized command.')
        bot.send_message(message.chat.id, '<b>You can just use the button.</b>', parse_mode='html')


bot.polling(none_stop=True)
