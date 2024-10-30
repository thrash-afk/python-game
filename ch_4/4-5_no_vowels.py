# Только согласные
# Демонстрирует, как создавать новые строки с помощью цикла for

message = input("\nВведите текст:\n")
new_message = ""
VOWELS = "aeiouаеёиоуыэюя"

print()

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Создана новая строка:", new_message)

print("Вот ваш текст без гласных букв:", new_message)
