temperature = int(input("What is the temperature in Fahrenheit? "))
if 110 > temperature > 90:
    print("It is hot outside.")
elif temperature >= 110:
    print('You could fry eggs out here.')
elif temperature < 30:
    print('It is cold outside.')
else:
    print('It is not hot outside.')
print("Done")