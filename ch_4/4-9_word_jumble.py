# Игра Анаграмма (Word Jumble)
# Компьютер выбирает какое-либо слово и хаотически расставляет в нем буквы
# Задача игрока - восстановить исходное слово

import random


# создадим последовательность слов из которых компьютер будет выбирать
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "пацаны", "сверхъестественное", "чудаки")

# случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)

# создадим переменную, с которой будет сопоставлена версия игрока
correct = word

# создаем анаграмму выбранного слова, в которой буквы расставлены хаотично
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# начало игры
print("\n\t\tДобро пожаловать в игру \"Анаграмма\"!")
print("\tНадо переставить буквы так, чтобы получилось осмысленное слово.")
print("\tДля выхода нажмите Enter, не вводя своей версии.")

print("Вот анаграмма:", jumble)

guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    print("К сожалению, вы не правы.")
    guess = input("\nПопробуйте отгадать исходное слово: ")

if guess == correct:
    print("\nСовершенно верно! Вы отгадали!\n")

print("Спасибо за игру.")
