# Автодилер
# Расчет стоимости автомобиля после всех наценок

car_price = int(input("Введите стоимость автомобиля без наценок:\n"))
tax = car_price * 0.18
reg_fee = car_price * 0.1
agent_fee = 15000
delivery = 10000

car_price_total = car_price + tax + reg_fee + agent_fee + delivery

print(f"\nНалог: {tax}")
print(f"\nРегострационный сбор: {reg_fee}")
print(f"\nАгентский сбор: {agent_fee}")
print(f"\nДоставка: {delivery}")
print(f"\n\nИтоговая цена автомобиля: {car_price_total}")
print()