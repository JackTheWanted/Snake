def discount(price,percent_discount):
    decimal_discount=percent_discount/100
    discount_amount=price*decimal_discount
    return price-discount_amount


cost=int(input('Please input the cost of your product:'))
discount_percent=int(input('Please input the % of your discount:'))
new_price=discount(cost,discount_percent)
print('The cost of your item after a', discount_percent,'% discount is $',new_price)

def