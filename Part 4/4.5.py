import random
my_number = random.randrange(100,201)
print(my_number)

my_list = ["rock", "paper", "scissors"]
random_index = random.randrange(3)
print(my_list[random_index])

my_number = random.random()* 5+10
print(my_number)

for num in range(10,4,-1):
    print ('Counting...', num)

import time
greeting = 'Hello World'
for letter in greeting:
    print (letter, end = '')
    time.sleep(1)

colour = ''
while colour.lower() != 'red':
    colour = input('What colour is Clifford?')
    if colour == 'red':
        print ('You win!')
    else:
        quit = input('Do you want to quit?')
        if quit == 'y':
            colour = 'red'
        if quit == 'n':
            colour = 'blue'