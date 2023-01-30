import controller


def create_csv():
    data = []
    with open('db.csv', 'w') as file:
        file.write (f'{data}')
    controller.user_choice()


def add_to_csv():
    name = input("Введите имя: ")
    surname = input('Введите Фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите коментарий: ')
    data = {
        "Name": name,
        "Surname": surname,
        "Phone number": phone,
        "Comment": comment,
    }
    new_data = open("db.scv",'a')
    data.append(new_data)
    with open("db.scv", "w") as file:
        data.write (f'{data["Surname"],data["Name"],data["Phone number"],data["Comment"]}')
    print('\nНовый контакт успешно добавлен!\n')
    controller.user_choice()