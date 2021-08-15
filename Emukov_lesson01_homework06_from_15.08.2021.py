a = int(input("Введите кол-во километров в 1 день "))
b = int(input("Введите кол-во требуемых километров "))
count_day = 0
while a < b:
    print(a)
    a = a * 1.1
    count_day += 1
else:
    print(a)
    count_day += 1
    print(count_day,"-й день")
