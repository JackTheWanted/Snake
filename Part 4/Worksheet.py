import random
#1
for i in range(10):
    print('Jack')
print('Done')

#2
count = 0
while count < 10:
    print('Jack')
    count += 1
print('Done')

#3
for i in range(20):
    print('Red')
    print('Gold')

#4
for i in range (2, 102, 2):
    print(i)

#5
count = 10
while count >= 0:
    print(count)
    count -= 1
print('BLAST OFF')

#6
print('This program takes in 3 integers and returns the sum. ')
total = 0
for i in range(3):
    x = int(input('Enter a number: '))
    total += x
print('The total is: ', total)

# 7
input("Hit ENTER for #7")
print(random.randint(1, 10))

# 8
input("Hit ENTER for #8")
print(random.uniform(1, 10))

# 9
input("Hit ENTER for #9")
total = 0
for i in range(7):
    x = int(input('Enter a number: '))
    total += x
print('The sum is: ', total)
print('The average is: ', total / 7)

# 10
input("Hit ENTER for #10")
heads = 0
tails = 0
for i in range(50):
    side = random.randint(0, 1)
    if side == 1:
        print("Heads")
        heads += 1
    elif side == 0:
        print("Tails")
        tails += 1
print('There were',heads,'heads.')
print('There were',tails,'tails.')
