def fix_punctuation_spaces(text):
    result = []
    fixed = False

    for i in range(len(text)):
        char = text[i]
        result.append(char)

        # Если текущий символ - знак препинания
        if char in ',.!?':
            # Проверяем следующий символ (если он есть)
            if i + 1 < len(text):
                next_char = text[i + 1]

                # Если следующий символ не пробел и не другой знак препинания
                if next_char != ' ' and next_char not in ',.!?':
                    result.append(' ')  # Добавляем пробел
                    fixed = True

    return ''.join(result), fixed


# Основная часть программы
print("Введите цитату:")
user_input = input()

fixed_text, was_fixed = fix_punctuation_spaces(user_input)

print("\nИсправленный текст:")
print(fixed_text)

if was_fixed:
    print("\n⚠️ Внимание: обнаружены пропущенные пробелы после знаков препинания и исправлены.")