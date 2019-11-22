def print_joke1():
    import time
    print('99 little bugs in the code')
    time.sleep(1)
    print('99 little bugs.')
    time.sleep(1)
    print('Fix a bug, run it again,')
    time.sleep(1)
    print("100 little bugs in the code.")

print('Press ENTER for a joke')
input()
print_joke1() #This 'calls' the function
#
# def print_joke2(num_bugs):
#     import time
#     print(num_bugs, 'little bugs in the code')
#     time.sleep(1)
#     print(num_bugs,'little bugs.')
#     time.sleep(1)
#     print('Fix a bug, link the fix in,')
#     time.sleep(1)
#     print(num_bugs + 1, 'little bugs in the code.')
# bugs=int(input('Input the number of bugs:'))
# print('Press ENTER for another joke')
# input()
# print_joke2(bugs)
# print()
