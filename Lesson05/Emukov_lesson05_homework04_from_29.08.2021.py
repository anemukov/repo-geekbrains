#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open("504-1.txt", encoding="UTF-8") as read_strings:

    print_strings = read_strings.readlines()

with open("504-2.txt", "w", encoding="UTF-8") as write_strings:

    for string in print_strings:
        el = string.split()
        el[0] = dictionary[el[0]]
        print(" ".join(el), file=write_strings)
