timeseconds = int(input("Введите время в секундах "))
hours = timeseconds // 3600
minutes = (timeseconds - hours * 3600) // 60
seconds = timeseconds - hours * 3600 - minutes * 60
print("%d:%02d:%02d" % (hours, minutes, seconds))
#print('{:d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
