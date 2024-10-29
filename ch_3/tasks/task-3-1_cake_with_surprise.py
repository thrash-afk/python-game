# Пирожок с "сюрпризом"

import random


surprise = random.randint(1, 5)

print("\n🎉 Ваш сюрприз:")
if surprise == 1:
    print("Поспать 🛏️")
elif surprise == 2:
    print("Деньги 💸")
elif surprise == 3:
    print("Авто 🚗")
elif surprise == 4:
    print("Мотоцикл 🏍️")
elif surprise == 5:
    print("Круиз на лайнере 🛳️")
else:
    print("Сегодня ничего не получите 🙁")