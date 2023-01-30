from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data


def greeting():
    print()
    print("Добро пожаловать в телефонный справочник!")

def input_data():
    idd=input('Введите id (порядковый номер): ')
    sename = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Комментарий: ")
    # phone_list=[idd, sename, first_name, middle_name, phone_number, note]
    return [idd, sename, first_name, middle_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep


def made_choice():
    print("Доступные операции с телефонной книгой:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта;\n\
    4 - сортировка.")
    while True:
        choice = input("Введите цифру: ")
        if choice == '1':
            sep = choice_sep()
            import_data(input_data(), sep)
        elif choice == '2':
            data = export_data()
            print_data(data)
        elif choice=='3':
            word = input("Введите данные для поиска: ")
            data = export_data()
            item = search_data(word, data)
            if item != None:
                print("id".center(20),"Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Телефон".center(15), "Категория".center(30))
                print("-"*130)
                print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15), item[5].center(30))
            else:
                print("Данные не обнаружены")
        elif choice=='4':
            data = export_data()
            sorted_by_id = sorted(data, key=lambda tup: tup[1])
            print_data(sorted_by_id)
        else:
            choice==''
            break    
        

        
        
    