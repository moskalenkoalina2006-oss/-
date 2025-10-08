print("Привет! Это мини-конвертер единиц измерения.")
print("Он поможет перевести значение из одной единицы в другую.\n")

while True:
    print("Выберите, что хотите конвертировать:")
    print("1. Метры в километры")
    print("2. Километры в метры")
    print("3. Градусы Цельсия в Фаренгейты")
    print("4. Градусы Фаренгейта в Цельсия")
    print("5. Выйти")

    choice = input("\nВаш выбор (введите номер): ")

    if choice == "5":
        print("Выход из программы. Хорошего дня!")
        break

    value = float(input("Введите значение для перевода: "))

    if choice == "1":
        result = value / 1000
        print(f"{value} метров = {result} километров\n")

    elif choice == "2":
        result = value * 1000
        print(f"{value} километров = {result} метров\n")

    elif choice == "3":
        result = (value * 9/5) + 32
        print(f"{value}°C = {result}°F\n")

    elif choice == "4":
        result = (value - 32) * 5/9
        print(f"{value}°F = {result}°C\n")

    else:
        print("Такого варианта нет, попробуйте снова.\n")
