# Счет по запросу
# Пользователь вводит начальные и конечные значения счета, и интервал

start = input("Введите начальное значение: ")

if not start:
    start = 0
start = int(start)

finish = input("Введите конечное значение: ")
while finish == "":
    finish = input("Введите конечное значение: ")
finish = int(finish)

step = input("Введите шаг счета:")
if step == "":
    step = 1
step = int(step)

for i in range(start, finish, step):
    print(i)
