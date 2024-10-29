# Отгадай число
#
# Компьютер выбирает случайное число в диапазоне от 1 до 100.
# Игрок пытается отгадать это число, и компьютер говорит,
# предположение больше/меньше, чем загаданное число или попало в точку

import random


print("\tДобро пожаловать в игру \"Отгадай число\"!")
print("\nЯ загадал натуральное число в диапазоне от 1 до 100.")
print("Постарайтесь угадать его за минимальное количество попыток.\n")

# Начальные значения
the_number = random.randint(1, 100)
guess = int(input("Ваше предположение: \n"))
tries = 1

# Цикл отгадывания
while the_number != guess:
    if the_number > guess:
        print("Больше")
    else:
        print("Меньше")
    guess = int(input("Ваше предположение: \n"))
    tries += 1

# Поздравляем победителя
print("\nВам удалось отгадать число! Это и в самом деле", the_number)
print("Вам понадобилось всего лишь", tries, "попыток!")

input("\n\nНажмите Enter, чтобы выйти.")