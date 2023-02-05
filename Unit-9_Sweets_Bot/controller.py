from telebot import types
import random
from main import bot
from veiw import user_turn, bot_turn

name1 = "User"
name2 = "bot"

@bot.message_handler(content_types = "text")
def controller(message):
    global flag, bot
    global name1, name2
    if message.text == "Узнать правила игры":
        bot.send_message(message.chat.id,"На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?")
    elif message.text == "Играть":
        bot.send_message(message.chat.id,"Начинаем")
        first_turn = random.choice([name1, name2])
        flag = name1 if first_turn == name1 else name2
        bot.register_next_step_handler(message,play)
    elif message.text == "Начать заново":
        restart(message)


def play(message):
    global a, sweets, max_sweet, flag
    if sweets>0:
        bot.send_message(message.chat.id,f"ходит {flag}, конфет осталось - {sweets}")
        if flag == name1:
                bot.send_message(message.chat.id,"Введите кол-во конфет от 1 до 28")
                bot.register_next_step_handler(message,user_turn)
        else:
                bot_turn(message)
    else:
        winner = name2 if flag == name1 else name1
        bot.send_message(message.chat.id,f"Поздравляем победил игрок {winner}")

def restart(message):
    global a, sweets, max_sweet, flag
    a = 0
    sweets = 221
    max_sweet = 28
    flag = name1