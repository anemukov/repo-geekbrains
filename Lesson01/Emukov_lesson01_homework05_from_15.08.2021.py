revenue = int(input("Введите значение выручки "))
expensive = int(input("Введите значение расходов "))
profit = revenue - expensive
profitability = (profit / revenue) * 100

if profit > 0:
    print("У Вас прибыль")
    print("Ваша рентабельность ", profitability, "%")
    persons = int(input("Введите количество сотрудников "))
    profit_for_person = profit / persons
    print("Прибыль на сотрудника ", profit_for_person, "рублей")
else:
    print("У Вас убыток")
