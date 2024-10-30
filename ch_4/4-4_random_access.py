# Случайные буквы
# Демонстрирует индексацию строк

import random


word = "индекс"
print("\nВ переменной word храниться слово:", word)
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])
