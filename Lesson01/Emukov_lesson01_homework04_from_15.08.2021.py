maxnumber = int(input("Введите целое число "))
x = 0
while maxnumber:
    if maxnumber % 10 > x:
        x = maxnumber % 10
    maxnumber //= 10
print(x)
