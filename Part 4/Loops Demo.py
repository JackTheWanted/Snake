
for i in range(9, -1, -1):
    for j in range(0, 9 - i):
        print(" ", end="")
    for j in range(0, i + 1):
        print(j, end="")
    print()
