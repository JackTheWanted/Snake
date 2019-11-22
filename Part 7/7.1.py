# my_bugs = ['flea', 'gnat', 'mosquito']
# my_bugs.append('dragon fly')
# my_bugs.insert(1,'house fly')
# print(my_bugs)
#
#
# my_list = [2, 4, 5, 6]
# print(my_list)
# my_list.append(9)
# print(my_list)
#
# my_list = [] # Empty list
# for i in range(5):
#     user_input = input( "Enter an integer: ")
#     user_input = int(user_input)
#     my_list.append(user_input)
#     print(my_list)

# Copy of the array to modify
my_list = [5, 100, 8, 5, 3, 3, 56, 5, 23]

# # Loop from 0 up to the number of elements
# # in the array:
# for i in range(9):
#     # Modify the element by doubling it
#     my_list[i] = my_list[i] * 2
#
# # Print the result
# print(my_list)
#
# x = "This is a sample string"
# # x = "0123456789"
#
# print("x=", x)
#
# # Accessing a single character
# print("x[0]=", x[0])
# print("x[1]=", x[1])
# print('x[2]=', x[2])
# print('x[3]=', x[3])
# # Accessing from the right side
# print("x[-1]=", x[-1])
#
# # Access 0-5
# print("x[:6]=", x[:6])
# # Access 6
# print("x[6:]=", x[6:])
# # Access 6-8
# print("x[6:9]=", x[6:9])

# a = "Hi There"
# print(len(a))
#
# b = [3, 4, 5, 6, 76, 4, 3, 3]
# print(len(b))
#
# for character in "This is a test.":
#     print(character)

# a = s = 'Hello'
# print('my string is ' + s)
# print('first letter is ' + s[0])
# b = 'There'
# print(a + b)
# print(len(a))
# print(len(a + b))

plain_text = input('Please input the text you want to encrypt:')

encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print('Encrypted text:', encrypted_text)

plain_text = ''

for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print('Deencrypted tex:', plain_text)