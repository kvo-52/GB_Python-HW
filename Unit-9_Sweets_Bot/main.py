import telebot
from telebot import types
import controller
import veiw



bot = telebot.TeleBot("6037289135:AAHbKnwzVW7jbv7feDN1AaHWlsnQ_7xpH_Q")

sweets = 221
max_sweet = 28
a = 0
name1 = "User"
name2 = "bot"
flag = name1


@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id,"/button")
    
@bot.message_handler(commands = ["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Узнать правила игры")
    but2 = types.KeyboardButton("Играть")
    but3 = types.KeyboardButton("Начать заново")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    bot.send_message(message.chat.id,"Выберай",reply_markup=markup)


controller.controller()
veiw.user_turn()
veiw.bot_turn()
controller.play()
controller.restart()


bot.infinity_polling()
