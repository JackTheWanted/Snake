# for i in range(0, 8):
#     print('*', end=' ')

for i in range(0,6):
    for j in range(0,6):
        print('*', end=' ')
    print()
#
# i = 0
# print(i, end=" ")
# i = 1
# print(i)
#
# for i in range(0,10):
#     print('*', end='')
# print()
# for j in range(0,5):
#     print('*', end='')
# print()
# for k in range(0,20):
#     print('*', end="")

# for i in range(0,5):
#     print('*', end="")
#     for j in range(0,20):
#         print('*', end='')
#     print()

# for i in range(10):
#     for j in range(10):
#         print(j,end='')
#     print()
#
# for i in range(10):
#     print(i+1, end='')
#     for j in range(10):
#         print(i+1, end='')
#     print()

# for row in range(10):
#
#     for j in range(row):
#         print(" ", end=" ")
#
#     for j in range(10 - row):
#         print(j, end=" ")
#
#     print()
#
# for row in range(10):
#     for j in range(10):
#         print(j, end='')
#     for j in range(row):
#         print(' ', end='')
#     print()

for i in range(10):
    for j in range(10 - i):
        print(" ", end = " ")
    for j in range(1, i + 1):
        print(j, end = " ")
    for j in range(i-1,0,-1):
        print(j, end = " ")

    print()