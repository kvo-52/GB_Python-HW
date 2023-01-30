# 38. Напишите программу, удаляющую из
# текста все слова содержащие "абв".

some_text = 'Кажабвдый абвигрок за кажабвдый ход абв можетабв взять не более M конфет '


def del_text(some_text):
    some_text = list(filter(lambda x: 'абв' not in x, some_text.split()))
    return " ".join(some_text)


some_text = del_text(some_text)
print(some_text)
