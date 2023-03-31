from datetime import datetime
a = str(datetime.today())
year = a[:4]
month = a[5:7]
day = a[8:10]
print(year, month, day, sep='\n')