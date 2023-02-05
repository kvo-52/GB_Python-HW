import random
from main import bot
from controller import play



@bot.message_handler(content_types = ["text"])
def user_turn(message):
    global a, sweets, flag, name1, name2    
    a = int(message.text)
    if 0<a<29:
        turn = a
        sweets -= turn
        if sweets>0:
            bot.send_message(message.chat.id,f'Конфет осталось - {sweets}')
        else:
            bot.send_message(message.chat.id,f'Конфет осталось - 0')
        flag = name2 if flag == name1 else name1
        play(message)
    else:
        print("Количество конфет от 1 до 28!!!")

@bot.message_handler(content_types = ["text"])
def bot_turn(message):
    global a, max_sweet, sweets, flag, name1, name2  
    turn = random.randint(1,max_sweet+1)
    bot.send_message(message.chat.id,f"bot взял {turn} конфет. ")
    sweets -= turn
    if sweets == 0:
        bot.send_message(message.chat.id,f'Конфет осталось - 0')
    flag = name2 if flag == name1 else name1
    play(message)