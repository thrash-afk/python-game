# Компьютерный датчик настроения
# Демонстрирует использование elif

import random


print("Я ощущаю вашу энергетику. От моего экрана не скрыто ни одно из ваших чувств.")
print("Итак ваше настроение...")

mood = random.randint(1, 3)
if mood == 1:
    # радостное
    print("""
        _________
       |         |
       | 0     0 |
       |    <    |
       |         |
       | .     . |
       |  `...`  |
        ---------    
                    """)
elif mood == 2:
    #  так себе
    print("""
        _________
       |         |
       | 0     0 |
       |    <    |
       |         |
       | ------- |
       |         |
        ---------    
                    """)
elif mood == 3:
    # прескверное
    print("""
        _________
       |         |
       | 0     0 |
       |    <    |
       |         |
       |   .'.   |
       |  `   `  |
        ---------    
                    """)
else:
    print("Не бывает такого настроения! (Должно быть, вы совершенно не в себе.)")

print("Но это только сегодня.")
input("\n\nНажмите Enter, чтобы выйти.")
