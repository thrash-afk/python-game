# Арсенал героя 3.0
# Демонстрирует работу со списками

# создадим список с несколькими элементами и выведем его с помощью цикла for
inventory = ["меч", "кольчуга", "щит", "целебное снадобье"]

print("\nИтак в вашем арсенале:")
for item in inventory:
    print(item)
input("Нажмите Enter, чтобы продолжить.")

# найдем длину списка
print("\nСейчас в вашем распоряжении", len(inventory), "предмета/ов.")
input("Нажмите Enter, чтобы продолжить.")

# проверка на пренадлежность к списку с помощью in
if "целебное снадобье" in inventory:
    print("\nВы еще поживете и повоюете.")

# вывод одного элемента с определенным индексом
index = int(input("\nВведите индекс одного из предметов арсенала: "))
print("Под индексом", index, "в арсенале находится", inventory[index], ".")

# отобразим срез
start = int(input("\nВведите начальный индекс среза: "))
finish = int(input("Введите конечный индекс среза: "))
print("Срез inventory[", start, ":", finish, "] - это", end=" ")
print(inventory[start:finish])
input("Нажмите Enter, чтобы продолжить.")

# соединим два списка
chest = ["золото", "драгоценные камни"]
print("\nВы нашли ларец. Вот что в нем:")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем снаряжении:")
print(inventory)
input("Нажмите Enter, чтобы продолжить.")

# присваиваем значение элементу списка
print("\nВы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print("Теперь ваш арсенал содержит следующие предметы:")
print(inventory)
input("Нажмите Enter, чтобы продолжить.")

# присвоение новых значений срезу списка
print("\nЗа золото и драгоценные камни вы купили магический кристалл, " \
      + "способный предсказывать будущее.")
inventory[4:6] = ["магический кристалл"]
print("Теперь в вашем распоряжении:")
print(inventory)
input("Нажмите Enter, чтобы продолжить.")

# удаляем элемент
print("\nВ тяжелом бою был раздроблен ваш щит.")
del inventory[2]
print("Вот что осталось в арсенале:")
print(inventory)
input("Нажмите Enter, чтобы продолжить.")

# удаляем срез
print("\nВоры украли у вас арбалет и кольчугу")
del inventory[:2]
print("В арсенале теперь только:")
print(inventory)
