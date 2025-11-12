def is_uppercase_letter(ch):
    return ch in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def is_letter(ch):
    return ch in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def is_digit(ch):
    return ch in "0123456789"

def clean_text(txt):
    punctuation = ".,:;!?«»\"'~$#@%^&*()_+-=<>/|{}[]"
    cleaned = ""
    for char in txt:
        if char in punctuation:
            cleaned += " "
        else:
            cleaned += char
    return cleaned

def count_words(uppercase_words):
    word_counts = {}
    for word in uppercase_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

text = """СРОЧНО! Это ВАЖНО! Все должны это видеть (а тем кто НЕ видел, СРОЧНО расскажите!!!111). НЕ игнорируйте — это РЕАЛЬНО спасёт жизни!
~СМС пришло в 3 часа. => Я был в ШОКЕ. ПОЖАЛУЙСТА, $$поделитесь$$! #ВАЖНО #СПАСИТЕ
P.S. Я не шучу. ПОВТОРЯЮ: ЭТО ВАЖНО!"""

cl_text = clean_text(text)
print("Очищенный текст:")
print(cl_text)
words = cl_text.split()
print("\nСписок слов:")
print(words)

uppercase_words = []
for word in words:
    if (len(word) >= 2 and
        all(is_uppercase_letter(ch) for ch in word) and
        not any(is_digit(ch) for ch in word)):
        uppercase_words.append(word)

print("\nСлова полностью заглавными буквами:")
print(uppercase_words)

word_counts = count_words(uppercase_words)

print("\nСлова полностью заглавными буквами и их частота:")
for word, count in word_counts.items():
    print(f"{word}: {count}")