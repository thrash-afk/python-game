# Компьютер отгадывает загаданное человеком число

print("\nЗагадайте число от 1 до 100.")
print("На вопрос компьютера отвечайте \"больше\", \"меньше\" или \"да\" без кавычек")

min_limit = 0
max_limit = 100
guess = 50
answer = ""

while True:
    print("Это число", guess, "?")
    answer = input()

    if answer == "больше":
        min_limit = guess
        guess += (max_limit - guess) // 2

    elif answer == "меньше":
        max_limit = guess
        guess -= (max_limit - min_limit) // 2
    elif answer == "да":
        break
    else:
        print("Я вас не понял. Повторите ввод.")

print(f"\nУра! Это число {guess}!")