import random
import datagen as gen

def get_start():
    word_list = gen.get_words()
    record = 0
    while True:
        lives = 5
        lvl = input("Выберите уровень сложности\n1. Легкий уровень\n2. Средний уровень\n3. Сложный уровень\n")
        if lvl == "1":
            lives = 7
        elif lvl == "2":
            lives = 5
        elif lvl == "3":
            lives = 3
        else:
            continue

        word = word_list.pop(random.randrange(len(word_list)))
        wish = ["■"] * len(word)
        print(''.join(wish))
        while ''.join(wish) != word:

            print(f"У вас {lives} жизней")

            if lives == 0:
                print("Ваши жизни закончились.\n")
                break

            letter = input("Введите букву или слово целиком\n")

            if letter.upper() in word and len(letter) == 1:
                for i in range(len(word)):
                    if word[i] == letter.upper():
                        wish[i] = letter.upper()
                print("вы отгадали букву!\n")
                print(''.join(wish))
                if ''.join(wish) == word:
                    print("Вы отгадали слово!\n")
                    record += 1

            elif letter.upper() == word and len(letter) == len(word):
                wish = word
                print("Вы отгадали слово!\n")
                record += 1

            elif letter.upper() != word and len(letter) != 1:
                lives = 0
                print(f"Вы назвали неправильное слово и проиграли. Загаданным словом было: {word}")

            elif letter.upper() not in word and len(letter) == 1:
                lives -= 1
                print("-1 жизнь. Попробуйте еще раз")

            elif letter == '' or letter == ' ':
                print("Введено некорректно")
                continue
            else:
                print("Введено некорреектно")
                continue

        if record > gen.get_records((record)):
            print("\nПоздравляем! Вы установили новый рекорд")
            print(f"Вы набрали: {record} очков.\nРекорд: {gen.get_records(record)}\n")

        if len(word_list) == 0:
            print("Слов больше не осталось")
            break

        rematch = input("Хотите ли вы сыграть еще раз?\nНажмите любую клавишу чтобы сыграть еще раз\nВведите 0 чтобы отказаться\n")
        if rematch == "0":
            break
        else:
            continue

if __name__ == "__main__":
    get_start()