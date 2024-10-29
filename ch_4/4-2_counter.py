# Считалка
# Демонстрирует использование функции range

print("\nПосчитаем:")
for i in range(10):
    print(i, end=" ")

print("\n\nПеречислим кратные пяти:")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nВ обратном порядке:")
for i in range(10, 0, -1):
    print(i, end=" ")

print()
for _ in range(10):
    print("Привет!")