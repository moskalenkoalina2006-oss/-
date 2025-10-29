def input_int(message):
    while True:
        user_input = input(message)
        if user_input.isnumeric() :
            input_int = int(user_input)
            if input_int == 0:
                print("Длина отрезка не может равняться 0. Введите данные снова!")
            else:
                return input_int
        else:
            print("Вы ввели не целое число. Попробуйте снова!")

def can_be_right_triangle(a, b, c):
    return (a**2 + b**2 == c**2)

a = input_int("Введите длину первого отрезка: ")
b = input_int("Введите длину второго отрезка: ")
c = input_int("Введите длину третьего отрезка: ")

if a > c: a, c = c, a
if b > c: b, c = c, b

print(f"Длинна первого отрезка  = {a}, длина второго отрезка = {b}, длина третьего отрезка = {c}")
if can_be_right_triangle(a, b, c):
    print("Из введённых отрезков можно построить прямоугольный треугольник")
else:
    print("Из введённых отрезков нельзя построить прямоугольный треугольник")