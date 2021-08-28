#7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.

import json

total = []
profit = {}
average_profit = []

with open("507-1.txt", encoding="UTF-8") as read_firm:

    counter = 1
    while True:
        list_firm = read_firm.readline().split()

        if not list_firm:
            break
        profit[list_firm[0]] = int(list_firm[2]) - int(list_firm[3])

        if profit[list_firm[0]] > 0:
            average_profit.append(profit[list_firm[0]])
        counter += 1

total = [profit, {"average_profit": sum(average_profit) / len(average_profit)}]

print(total)

with open("507-2.json", "w", encoding="UTF-8") as json_write:
    json.dump(total, json_write)

    #for firm in list_firm:
        #num_str = firm.split()
        #profit = int(num_str[2])-int(num_str[3])
        #print(f"Прибыль компании {num_str[1]} {num_str[0]} = {profit}")
        #if int(profit) > 0:
            #print(profit)
        #z += 1
    #sum_profit = sum(profit)

    #print(f"Средняя прибыль компаний = {sum_profit/z}")