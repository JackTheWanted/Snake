age = int(input("Input an age:"))
name = input("Your name?")
shoe_size = float(input('Input your shoe size as a decimal number:'))
print('%s is %d with a shoe size of %4.1f' % (name,age,shoe_size))
#Date and Time
from datetime import date
print(date.today())
from datetime import datetime
now=datetime.now()
print('Date is %s/%s/%s' %(now.month, now.day, now.year))
print('The time is %s:%s:%s' % (now.hour, now.minute, now.second))
