import telebot
from telebot import types

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather
bot = telebot.TeleBot('6547147398:AAHoOdqQSZK5qnV9Xc6UMVwbM1DHMXb8vy0')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        # Image link
        image_link = "https://graph.org/file/4a28115623583037911d0.jpg"  # Replace with your image link
        
        # Caption with Banknifty Mentor
        caption = """You are just 1 step away from joining Banknifty Mentor official telegram channel 🎯🎯🚀🚀

Get Daily FREE trading calls in Banknifty, nifty, Zero To Hero & stock options

✅ Trusted by 10,000+ traders
✅ All Trades Comes with Proper Target and Stoploss
✅ Live market update in Each and every Trades
✅ Daily market Analysis

👇 Click on below button to join our Telegram channel 👇"""

        # Creating an inline keyboard markup with a button that redirects to the specified link
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Join Banknifty Mentor Now", url="https://t.me/+MeoBVj7Flb1lN2Y9"))

        # Sending the photo with the caption and the inline keyboard markup
        bot.send_photo(message.chat.id, image_link, caption=caption, reply_markup=markup)
    except telebot.apihelper.ApiTelegramException as e:
        if e.error_code == 403:
            print("Bot was blocked by the user:", e)
        else:
            print("Error sending welcome message:", e)
    except Exception as e:
        print("Error sending welcome message:", e)

# Start the bot
bot.polling()
