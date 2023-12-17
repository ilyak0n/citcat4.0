from random import randrange

count = 0
guess = randrange(0,101)
print("Число загадно, сможешь отгадать?")

while True:
    user = input()
    if user.isdigit():
        if int(user) > guess:
            print("Ваше число больше!")
            count += 1
        elif int(user) < guess:
            print("Ваше число меньше!")
            count += 1
        elif int(user) == guess:
            count += 1
            print(f"Поздравляем! Вы угадали число за {count} попытки")
    else:
        print("Вы должны угадывать число, а не что-то другое!")
        continue