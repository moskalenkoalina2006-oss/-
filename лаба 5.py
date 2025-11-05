# Функция для ввода имени
def input_name(name: str, len_name: int):
  while True:
    value = input(f"Введите {name}: ").strip()
    if value == "":
      print(f"⚠️ {name} не может быть пустым!")
      continue
    if len(value) < len_name:
      print(f"⚠️ {name} должно содержать минимум {len_name} символа!")
      continue
    return value

# Функция для ввода фамилии
def input_surname(surname: str, len_surname: int):
  while True:
    value = input(f"Введите {surname}: ").strip()
    if value == "":
      print(f"⚠️ {surname} не может быть пустым!")
      continue
    if len(value) < len_surname:
      print(f"⚠️ {surname} должно содержать минимум {len_surname} символа!")
      continue
    return value

# Функция для ввода возраста
def input_age():
  while True:
    age_input = input("Возраст: ").strip()
    try:
      age = int(age_input)
      if age < 18:
        print("⚠️ Возраст должен быть не менее 18 лет!")
        continue
      elif age > 90:
        print("⚠️ Возраст должен быть не более 90 лет!")
        continue

      return age

    except ValueError:
      print("⚠️ Введите число!")

# Функция для ввода формы участия
def input_online_offline():
  while True:
    value = input("Вы будете учавствовать онлайн или офлайн? (Введите 'онлайн' или 'офлайн'): ").strip().lower()
    if value in ["онлайн", "офлайн"]:
      return value
    else:
      print("⚠️ Выберите 'онлайн' или 'офлайн'")

# Функция для вывода билета участника
def print_survey(participant):
  print()
  print("-" * 40)
  print("----- ДАННЫЕ УЧАСТНИКА КОНФЕРЕНЦИИ -----")
  print("-" * 40)
  print(f"Имя:           {participant['name']}")
  print(f"Возраст:       {participant['age']} лет")
  print(f"Фамилия:       {participant['surname']}")
  print(f"Фарма участия: {participant['form_of_participation']}")
  print("-" * 40)
  print()

# Главная функция для ввода данных и вывода результата
def survey():

    print("-" * 40)
    print("----- ДАННЫЕ УЧАСТНИКА КОНФЕРЕНЦИИ -----")
    print("-" * 40)
    print()

    participant = {}
    # 1. Ввод имени (не должно быть пустым)
    participant["name"] = input_name("Имя", 2)
    # 2. Ввод фамилии (не должен быть пустым)
    participant["surname"] = input_surname("Фамилия", 2)
    # 3. Ввод возраста (должно быть числом от 18 до 90)
    participant["age"] = input_age()
    # 4. Ввод формы участия(да/нет)
    participant["form_of_participation"] = input_online_offline()

    # Вывод всех данных красиво
    print_survey(participant)
    print("✅ Данные сохранены!")

    return participant


# Запуск программы
result = survey()
print(f"\nСпасибо, {result['name']}! Вы зарегестрированы.")