from random import randrange

def bdays(n,k):
    count = 1
    for i in range(n):
        m = []
        for j in range(k):
            m.append(randrange(1,366))
        mn = set(m)
        if len(mn) < len(m):
            count += 1
    return f"Проент совпадения дней рождения в {k} группах из {n} сучаев: {count/n}%"

def main():
    print(bdays(1000,23))

if __name__ == "__main__":
    main()