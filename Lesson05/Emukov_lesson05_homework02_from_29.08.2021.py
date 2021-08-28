#2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("502.txt", encoding="UTF-8") as try_count:

    lines = try_count.readlines()
    for line in lines:
        print(line.replace("\n", " "))
    print(f"\nВ файле {len(lines)} строк", "\n")

    words = 1
    for string in lines:
        print(f"В строке {words}: {len(string.split())} слов")
        words += 1








