def give_money1(money):
    money += 100


class Person():
    def __init__(self):
        self.name = ""
        self.money = 0




bob = Person()
bob.name = "Bob"
bob.money = 100

give_money1(bob.money)
print(bob.money)


class Boat():
    def __init__(self):
        self.tonnage = 0
        self.name = ""
        self.is_docked = True

    def dock(self):
        if self.is_docked:
            print("You are already docked.")
        else:
            self.is_docked = True
            print("Docking")

    def undock(self):
        if not self.is_docked:
            print("You aren't docked.")
        else:
            self.is_docked = False
            print("Undocking")

