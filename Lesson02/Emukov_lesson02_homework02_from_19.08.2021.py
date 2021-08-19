#2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_elements = []
input_elements = (input("Введите значения "))
list_elements.extend(input_elements)
print("Введенный список", list_elements)

for x in range(0, len(list_elements)-1, 2):
        list_elements[x], list_elements[x+1] = list_elements[x+1], list_elements[x]

print("Измененный список", list_elements)


