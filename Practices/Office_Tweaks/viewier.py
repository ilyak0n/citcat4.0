from defs import *
import os


def show():
    a = True
    while a:
        print(f"Текущий каталог: {os.getcwd()}\
              \nВыберите действие: \n\
              \n0) Сменить рабочий каталог\
              \n1) Преобразовать PDF в Docx\
              \n2) Преобразовать Docx в PDF\
              \n3) Произвести сжатие изображений\
              \n4) Удалить группу файлов\
              \n5) Выход\n")

        choose = input("Ваш выбор: ")

        if choose == "0":
            change_catalog()

        elif choose == "1":
            print("Список файлов с расширением .pdf в этом каталоге: \n")
            pdf2docx()

        elif choose == "2":
            print("Список файлов с расширением .docx в этом каталоге: \n")
            docx2pdf()

        elif choose == "3":
            print("Список файлов с расширениями ('.jpeg', '.gif', '.png', '.jpg') в данном каталоге: \n")
            image_convertation()

        elif choose == "4":
            print("Выберите действие: \
                  \n1) Удалить все файлы, начинающиеся на определенную подстроку\
                  \n2) Удалить все файлы, заканчивающиеся на определенную подстроку\
                  \n3) Удалить все файлы, содержащие определенную подстроку\
                  \n4) Удалить все файлы по расширению\n")

            second_choose = input("Введите номер действия: ")

            if second_choose == "1":
                start_delete()
                print("\n")

            elif second_choose == "2":
                end_delete()
                print("\n")

            elif second_choose == "3":
                in_delete()
                print("\n")

            elif second_choose == "4":
                expansion_delete()
                print("\n")

            else:
                continue

        elif choose == "5":
            a = False

        else:
            continue

if __name__ == "__main__":
    show()

