#5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

list_write = []
input_numbers = input("Введите числа через пробел ")
list_write.append(str(input_numbers))

with open("505.txt", "w") as write_numbers:
    print(f'{" ".join(list_write)}', file=write_numbers)

with open("505.txt") as read_numbers:

    numbers = read_numbers.readline().split()
    sum_numbers = 0

    for number in numbers:
        sum_numbers += int(number)
    print(f"Сумма чисел в файле = {sum_numbers}")