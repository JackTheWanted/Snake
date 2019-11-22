#Jack C
from datetime import date
print(date.today())
from datetime import datetime

def discount(price,percent_discount):
    decimal_discount=percent_discount/100
    discount_amount=price*decimal_discount
    return price - discount_amount

def total_price(new_price):
    return new_price*1.13



now=datetime.now()
print('It is the %sth day of the %sth month of %s.' %(now.day,now.month, now.year))
print('Right now it is %s:0%s and %s seconds have passed.' % (now.hour, now.minute, now.second))

#Purchases with Tax
name=input("Your name:")
print("Please enter the prices of 2 items your purchased from the Quickie Mart.")
first_item = float(input("First Item Price:"))
second_item = float(input("Second Item Price:"))
total = (first_item+second_item)*1.13
tax = (total-first_item)-second_item
print('Your name is %s, your total purchase was $%0.2f, and $%0.2f of that was in tax' % (name, total, tax))



cost = float(input('Please input the cost of your product:'))
discount_percent = float(input('Please input the % of your discount:'))
new_price = discount(cost,discount_percent)
print('The cost of your item after a %0.0f%% discount is $%0.2f' %(discount_percent, new_price))



print('With the discount and the taxes, the overall cost is $%0.2f'%(total_price(new_price)))


