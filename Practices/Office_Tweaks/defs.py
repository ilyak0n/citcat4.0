import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image

def change_catalog():
    os.chdir(input("Укажите корректный путь к рабочему каталогу: "))

def pdf2docx():
    pdf_file_list = []
    for i in range(len(os.listdir(os.getcwd()))):
        if os.listdir(os.getcwd())[i][-4:] == ".pdf":
            pdf_file_list.append(os.listdir(os.getcwd())[i])
    for i in range(len(pdf_file_list)):
        print(f"{i+1} {pdf_file_list[i]}")

    number = int(input("\nВведите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): "))
    if number != 0:
        for i in range(len(pdf_file_list)):
            if i+1 == number:
                pdf_file = (pdf_file_list[i])
                docx_file = (str(pdf_file[:-4])+".docx")
                cv = Converter(pdf_file)
                cv.convert(docx_file)
                cv.close()
    else:
        for i in range(len(pdf_file_list)):
            pdf_file = (pdf_file_list[i])
            docx_file = (str(pdf_file[:-4])+".docx")
            cv = Converter(pdf_file)
            cv.convert(docx_file)
            cv.close()

def docx2pdf():
    docx_file_list = []
    for i in range(len(os.listdir(os.getcwd()))):
        if os.listdir(os.getcwd())[i][-5:] == ".docx":
            docx_file_list.append(os.listdir(os.getcwd())[i])
    for i in range(len(docx_file_list)):
        print(f"{i + 1} {docx_file_list[i]}")

    number = int(input("\nВведите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): "))
    if number != 0:
        for i in range(len(docx_file_list)):
            if i+1 == number:
                convert(docx_file_list[i], docx_file_list[i][:-5]+".pdf")
    else:
        for i in range(len(docx_file_list)):
            convert(docx_file_list[i], docx_file_list[i][:-5]+".pdf")

def image_convertation():
    image_file_list = []
    for i in range(len(os.listdir(os.getcwd()))):
        if os.listdir(os.getcwd())[i][-5:] == ".jpeg" or os.listdir(os.getcwd())[i][-4:] == ".gif" or os.listdir(os.getcwd())[i][-4:] == ".png" or os.listdir(os.getcwd())[i][-4:] == ".jpg":
            image_file_list.append(os.listdir(os.getcwd())[i])
    for i in range(len(image_file_list)):
        print(f"{i + 1} {image_file_list[i]}")

    number = int(input("\nВведите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): "))
    if number != 0:
        for i in range(len(image_file_list)):
            if i+1 == number:
                qual = int(input("Введите параметры сжатия (от 0 до 100%): "))
                image_file = Image.open(image_file_list[i])
                image_file.save(image_file_list[i], quality=qual)
    else:
        for i in range(len(image_file_list)):
            qual = int(input("Введите параметры сжатия (от 0 до 100%): "))
            image_file = Image.open(image_file_list[i])
            image_file.save(image_file_list[i], quality=qual)


def start_delete():
    s = input("Введите подстроку, с которой должны начинаться файлы: ")
    for file in os.listdir(os.getcwd()):
        if file.startswith(s):
            os.remove(os.path.join(os.getcwd(), file))
            print(f"Файл: '{os.path.join(os.getcwd(), file)}' успешно удален!")

def end_delete():
    s = input("Введите подстроку, которой должны заканчиваться файлы: ")
    for file in os.listdir(os.getcwd()):
        if file.endswith(s):
            os.remove(os.path.join(os.getcwd(), file))
            print(f"Файл: '{os.path.join(os.getcwd(), file)}' успешно удален!")

def in_delete():
    s = input("Введите подстроку, которая должна содержаться в файлах: ")
    for file in os.listdir(os.getcwd()):
        if s in file:
            os.remove(os.path.join(os.getcwd(), file))
            print(f"Файл: '{os.path.join(os.getcwd(), file)}' успешно удален!")

def expansion_delete():
    s = input("Введите расширение файлов, которые хотите удалить: ")
    for file in os.listdir(os.getcwd()):
        if file.endswith(s):
            os.remove(os.path.join(os.getcwd(), file))
            print(f"Файл: '{os.path.join(os.getcwd(), file)}' успешно удален!")

def main():
    print()