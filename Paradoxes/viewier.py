from first import *
from second import *

def show():
    print("Выберите парадокс")
    print("1. Парадокс Монти Холла\
          \n2. Парадокс дней рождений")
    ch = input()
    if ch == "1":
        ab = input("Введите количество итераций: ")
        if ab.isdigit():
            print(monty_hall(int(ab)))
        elif ab == "":
            print(monty_hall(10000))
        else:
            show()
    elif ch == "2":
        ba = input("Введите количество итераций: ")
        bab = input("Введите количетсво групп: ")
        if ba.isdigit() and bab.isdigit():
            print(bdays(int(ba), int(bab)))
        elif ba == "" and bab == "":
            print(bdays(1000,23))
        else:
            show()
    else:
        show()

if __name__ == "__main__":
    show()