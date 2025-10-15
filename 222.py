name = input("Введите ваше имя: ")
message =input("Опишите ваше состояние: ")
stress = int(input("Введите балл по шкале тревоги от 20 до 80: "))

print("\n")
print("_"*50)
print("РЕЗУЛЬТАТ АНАЛИЗА УРОВНЯ СТРЕССА")
print("_"*50)
print(f"Имя: {name}")
print(f"Сообщение: {message}")
print("\n")

print("АНАЛИЗ МАРКЕРОВ СТРЕССА")

has_anxiety = (
    "тревог" in message or
    "страх" in message or
    "боюсь" in message or
    "паник" in message)

has_positive = ("надежд" in message or
                "спокойств" in message or
                "радост" in message)
if has_anxiety and has_positive:
    print("Смешанные или нейтральные эмоции")
elif has_anxiety:
    print("Обнаружены признаки тревоги")
elif has_positive:
    print("Текст имеет позитивную окраску")
print("\n")

print("АНАЛИЗ ЧИСЛОВОЙ ОЦЕНКИ СТРЕССА")

if stress <= 30 :
    stress_level = "низкий"
elif  31<=stress<=44 :
    stress_level = "умеренный"
else:
    stress_level = "высокий"

print(f"Оценка стресса: {stress} - > {stress_level}")
print("Итог")

if has_anxiety and stress >=45 :
    print("Рекомендуется срочная психологическая поддержка")
else:
    print("Состояние в пределах ожидаемого. Продолжайте наблюдение")