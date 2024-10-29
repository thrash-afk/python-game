# Орел или решка
# Подбрасываем монету 100 раз и узнаем сколько раз выпал орел, а сколько раз - решка

import random


print("\nПодбрасываем монету 🪙  100 раз")
tries = 0
heads = 0
tails = 0
something_wrong = 0

while tries < 100:
    result = random.randrange(2)
    if result == 1:
        heads += 1
    elif result == 0:
        tails += 1
    else:
        something_wrong += 1
    tries += 1

print("\n▶️ Орел выпал", heads, "раз.")
print("▶️ Решка выпала", tails, "раз.")
print("Что-то пошло не так", something_wrong, "раз.")
