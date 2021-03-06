print('Задача 7. Великий и могучий')

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Особенно Паоло понравилась книга “Преступление и наказание”.
# И ему стало интересно,
# какое можно найти самое длинное слово в этой книге, чтобы потом сравнить его с аналогом на своём языке.
#
# Напишите программу,
# которая получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
#
# Пример:
# Введите текст: Меня зовут Петр
# Длина самого длинного слова: 5

sequence = 0
maxSymbol = 0

text = input("Введите текст: ")

for symbol in text:
    if symbol != " ":
        sequence += 1
    elif maxSymbol < sequence:
        maxSymbol = sequence
        sequence = 0
    else:
        sequence = 0
if maxSymbol < sequence:
    maxSymbol = sequence

print(f"Длина самого длинного слова: {maxSymbol}")
