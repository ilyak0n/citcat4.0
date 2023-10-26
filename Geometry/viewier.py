def show():
    print("Выберите функцию: ")
    print("1. Площадь квадрата \
          \n2. Площадь прямоугольника\
          \n3. Площадь треугольнка\
          \n4. Периметр любой геометрической фигуры")
    c = input()

    if c == "1":
        print(f"Площадь квадрата: {sq_sq(float(input('Введите длину стороны а: ')))}")
    elif c == "2":
        print(f"Площадь прямоугольника: {sq_pr(float(input('Введите длину стороны а: ')), float(input('Введите длину стороны b: ')))}")
    elif c == "3":
        print(f"Площадь треугольника: {sq_tr(float(input('Введите длину стороны b: ')), float(input('Введите длину высоты h: ')))}")
    elif c == "4":
        print(f"Периметр любой геометрической фигуры: {get_perimetr(*[float(i) for i in input('Введите длины через пробел: ').split()])}")


if __name__ == "__main__":
    from square import *
    from perimetr import *
    show()
else:
    from .square import *
    from .perimetr import *
