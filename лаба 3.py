#1 Создать список реплик
speeches = ["Я помню чудное мгновение.",
            "Каждый день прекрасен.",
            "Я сказал, что люблю гулять в саду после дождя.",
            "Осенняя погода начала становиться всё дождливее и холоднее.",
            "Мама оказалась около меня как раз в нужный момент.",
            "Я остался совсем один без какой-либо поддержки"
]

#2 Добавить новую реплику
speeches.append("Мама гуляла весь вечер в саду")

#3 Вывести каждую 2 реплику
for speech in range(1, len(speeches), 2) :
    print(speeches[speech])


#4 Найти самую короткую реплику
print("_" * 50)
shortest= speeches[0]
for speech in speeches :
    if len(shortest)>len(speech):
        shortest = speech
print("Самая короткая реплика: ", shortest)
print("_" * 50)

#5 Посчитать сколько реплик начинается с буквы "Я"
count=0
for speech in speeches :
    if "Я" in speech:
        count=count+1
print(f"Количество реплик, которые начинаются на 'Я': {count}")
print("_" * 50)

#6 Вывести на печать все реплики, в которых встречается слово "сказал"
for speech in speeches :
    if 'сказал' in speech:
         print(speech)