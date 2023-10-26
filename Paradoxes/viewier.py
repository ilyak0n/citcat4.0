def start():
    print("Выберите парадокс")
    print("1. Парадокс Монти Холла\
          \n2. Парадокс дней рождений")
    ch = input()

    if ch == "1":
        print(f"Процент побед в двух случаях: {monty_hall(int(input('Введите количество раз: ')))}")
    elif ch == "2":
        print(f"Процент совпадения дней рождений: {bdays(int(input('Введите количество раз: ')), int(input('Введите количество групп: ')))}")


if __name__ == "__main__":
    from first import *
    from second import *
    start()
else:
    from .first import *
    from .second import *