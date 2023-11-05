from random import randrange

def monty_hall(n):
    win1 = 0
    win2 = 0
    games = 0
    a = [1, 2, 3]
    for i in range(n):
        win = randrange(1, 4)
        a[win - 1] = "$"
        player = randrange(1, 4)
        a[player - 1] = "X"
        non = randrange(1, 4)
        if non == win and non == player:
            while non == win and non == player: non = randrange(1, 4)
        a[non - 1] = "-"
        if a.index(a[player - 1]) == a.index(a[win - 1]):
            win1 += 1
            games += 1
        elif a.index(a[win - 1]) != a.index(a[player - 1]):
            win2 += 1
            games += 1
    return f"Процент победы при неизменном выборе: {win1/games}%\
           \nПроцент победы после смены выбора: {win2/games}%"

def main():
    print(monty_hall(10_000))

if __name__ == "__main__":
    main()