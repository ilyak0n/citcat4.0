try:
    path = input("Введите имя файла: ").strip()
    file = open(path)
    file.seek(3)
    file_list = [int(x) for x in file.readlines()]
    print(file_list)

except FileNotFoundError:
    print("Введите правильное название файла!")

except ValueError:
    print("Проверьте символы в файле!")

except OSError:
    print("Ошибка операционной системы")

except:
    print("Произошла непредвиденная ошибка")

finally:
    print('')