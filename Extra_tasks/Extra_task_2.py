num_book = {}
def view_book(): #Функция №2
    return num_book
def new_contact(): #Функция №1
    while True:
        print("Введите имя и фамилию")
        name = input()
        if name.count(" ") == 1:
            b = name[0]
            x = name[name.find(" ") + 1]
            name = b.upper() + name[1:name.find(" ") + 1] + x.upper() + name[name.find(" ") + 1+1:]
            print("Теперь введите номер")
            num = input()
            if num[0] == "8" or "7" or "+7":
                if num[:2] != "+7":
                    num = num.replace(num[0],"+7",1)
                if num.count(" ") != 0:
                    num = num.replace(" ","")
                if len(num) != 12:
                    print("Введите заново")
                else:
                    num_book[name] = num
                    break
            else:
                print("Введите заново")
                continue
        else:
            print("Введено неверно")
            continue
def del_contact(): # Функция №3
    while True:
        print(num_book)
        print("Выберите имя контакта, который хотите удалить")
        name = input()
        b = name[0]
        x = name[name.find(" ") + 1]
        name = b.upper() + name[1:name.find(" ") + 1] + x.upper() + name[name.find(" ") + 1+1:]
        if name not in num_book:
            print("Неверно введено имя")
            continue
        else:
            print(num_book.pop(name))
            break
def change_contact(): #Функция №4
    while True:
        print(num_book)
        print("Выберите имя контакта, номер которого вы хотите изменить")
        name = input()
        b = name[0]
        x = name[name.find(" ") + 1]
        name = b.upper() + name[1:name.find(" ") + 1] + x.upper() + name[name.find(" ") + 1+1:]
        if name in num_book:
            print("Введите новый номер")
            num = input()
            if num[0] == "8" or "7" or "+7":
                if num[:2] != "+7":
                    num = num.replace(num[0],"+7",1)
                if num.count(" ") != 0:
                    num = num.replace(" ","")
                if len(num) != 12:
                    print("Введите заново")
                else:
                    num_book[name] = num
                    break
            else:
                print("Введите заново")
                continue
        else:
            print("Неверно введено имя")
            continue
while True:
    print("")
    print("Выберите команду")
    print("1. Добавить контакт")
    print("2. Посмотреть контакты")
    print("3. Удалить контакт (по имени)")
    print("4. Изменить номер телефона (по имени)")
    komand = input()
    if komand == "1":
        new_contact()
    elif komand == "2":
        print(view_book())
    elif komand == "3":
        del_contact()
    elif komand == "4":
        change_contact()
    elif komand == "close":
        break
    else:
        continue