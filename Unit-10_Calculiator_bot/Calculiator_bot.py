import telebot
from telebot import types
from datetime import datetime as dt

bot = telebot.TeleBot("TOKEN")
time_sign = dt.now().strftime('%D %H:%M')

a = 0
b = 0
znak = ""

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Тебя приветсвует калькулятор!")
    button(message)

@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Целые числа")
    but2 = types.KeyboardButton("Комплексные числа")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Выберите режим работы калькулятора", reply_markup=markup)

@bot.message_handler(content_types="text")
def controller(message):
    if message.text == "Целые числа":
        bot.send_message(message.chat.id, "Введите два числа через пробел")
        log(message)
        bot.register_next_step_handler(message, user_int_numbers)
    elif message.text == "Комплексные числа":
        bot.send_message(message.chat.id, "Введите два комплексных числа через пробел. Пример: 2+3j 4+5j")
        log(message)
        bot.register_next_step_handler(message, user_complex_numbers)

def log(message):
    file = open('db.csv', 'a')
    file.write(f'{time_sign},{message.chat.username},{message.chat.id},{message.text}\n')
    file.close()    

def user_int_numbers(message):
    global a,b
    log(message)
    numbers = message.text
    a = int(numbers.split()[0])
    b = int(numbers.split()[1])
    button_znaki_int(message)

def user_complex_numbers(message):
    global a,b
    log(message)
    numbers = message.text
    a = complex(numbers.split()[0])
    b = complex(numbers.split()[1])
    button_znaki_complex(message)

def button_znaki_int(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("+")
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("*")
    but4 = types.KeyboardButton("/")
    but5 = types.KeyboardButton("%")
    but6 = types.KeyboardButton("//")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    markup.add(but5)
    markup.add(but6)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)
    bot.register_next_step_handler(message, operators)

def button_znaki_complex(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("+")
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("*")
    but4 = types.KeyboardButton("/")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)
    bot.register_next_step_handler(message, operators)

@bot.message_handler(content_types="text")
def operators(message):
    global a,b
    log(message)
    result = 0
    if message.text == "+":
        result = a + b
        bot.send_message(message.chat.id, f'{a} + {b} = {result}')
    elif message.text == "-":
        result = a - b
        bot.send_message(message.chat.id, f'{a} - {b} = {result}')
    elif message.text == "*":
        result = a * b
        bot.send_message(message.chat.id, f'{a} * {b} = {result}')
    elif message.text == "/":
        result = a / b
        bot.send_message(message.chat.id, f'{a} / {b} = {result}')
    elif message.text == "%":
        result = a % b
        bot.send_message(message.chat.id, f'{a} % {b} = {result}')
    elif message.text == "//":
        result = a // b
        bot.send_message(message.chat.id, f'{a} // {b} = {result}')

bot.infinity_polling()