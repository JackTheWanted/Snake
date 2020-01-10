#Jack C
mac = 1520
babysitting = 125
allowance = 135
total = int(mac+babysitting+allowance)
print("$",total)


first = input("First name:")
last = input("Last name:")
wage = float(input("Hourly wage:"))
time = float(input("Hours worked:"))
print(first, last)
total_wage = (wage*time)
print("$",total_wage)


#Gonna do the area calculation for traingle
print("To determine the area of your triangle, please prepare the following values(cm):base, height.")
height = float(input("Height:"))
base = float(input("Base:"))
area = (base*height)/2
print("Area=",area, "cm2")
