# Угадай слово
# Компьютер загадывает слово и сообщает его длину, а игрок должен его угадать.
# У игрока есть 5 попыток узнать, есть ли какая-либо буква в загаданном слове.

import random


WORDS = ("принц", "мама", "папа", "сестра", "дочь", "брат", "утро", "вечер")
word = random.choice(WORDS)
tries = 5
i = 1
letters = ()

print(f"\nЯ загадал слово из {len(word)} букв. У тебя есть {tries} попыток узнать, " \
      + "\nесть ли какая-либо буква в загаданном слове." \
        + "\nЯ буду отвечать только \"Да\" или \"Нет\" ")

while tries:
    print("Попытка узнать букву №", i)
    letter = input("Введите букву: ")
    if len(letter) > 1 or letter == "":
        print("Нужно ввести ОДНУ букву.")
    else:
        tries -= 1
        i += 1
        if letter in word:
            print("Да")
            if letter not in letters:
                letters += tuple(letter)
        else:
            print("Нет")

print("Итак, в этом слове есть буквы", letters)
print("Слово из", len(word), "букв.")
print("Для выхода нажмите Enter, не вводя вариант ответа.\n")

guess = input("Что это за слово?\n")
while guess != word and guess != "":
    print("\nЭто не то слово.")
    guess = input("Что это за слово?\n")

if guess == word:
    print("\nПоздравляю, это действительно слово:", word.upper())

print("Спасибо за игру.")
