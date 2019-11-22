#Jack C

#1
i = 0
total = 0
score = [0, 0, 0, 0, 0, 0]
for i in range(len(score)):
     score = int(input('Please input your scores: '))
     total += score
     i += 1

print('Scores average to:', total/i)

#2
i = 0
names = []
for i in range(6):
    names.append(input('Input the 6 names:'))
    names.sort()

print(names[0], names[1], names[2], names[3], names[4], names[5])

for i in range(3):
    names.append(input('Input 3 more names:'))
    names.sort()

print(names[0], names[1], names[2], names[3], names[4], names[5], names[6], names[7], names[8])