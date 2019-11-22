#Jack C
import random

#1
year = 1912
for year in range(year, 1955):
    print(year)
    year += 1
print('The life of Turing')

#2
time = int(input('Please input a number between 5 and 10:'))
if time >= 5 and time <= 10:
    while time > 0:
        print(time)
        time -= 1
    print('Blast Off!')
else:
    print('You didn\'t input a number between 5 and 10, idiot.')

#3
for i in range(5):
    random_num = random.randrange(1, 22)
    if random_num % 3 == 0:
        print(random_num, 'is divisible by 3.')

