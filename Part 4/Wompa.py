#Jack C
import random
import time

def instructions():
    print('Hoth Survival GAME:'
          '\n  As a warrior in the Rebel Army, you have destroyed a hanger full of Galactic'
          '\nFighters and then stole a wompa to escape across the vast frozen tundra to'
          '\nfreedom. The Empire is chasing you down to kill you! Survive your ice desert'
          '\ntrek and outsmart them all!')


def menu():
    print('You have the following options:'
    '\n-------------------------------'
    '\nA: Eat a chocolate bar from your food pack.'
    '\nB: Ahead moderate speed.'
    '\nC: Ahead full speed.'
    '\nD: Stop and rest.'
    '\nQ: Quit.')
    choice = input().lower()
    return choice


a = 0
b = 0
c = 0
d = 0
q =0
km_travelled = 0
hunger = 0
wompa_tiredness = 0
enemy_distance= -20
chocolate_bars = 3
chance = 0
done = False

print('Press ENTER for the instructions.')
input()
instructions()
print()
input('Press any key to begin the game.')
while not done:
    print()
    print('Kilometers travelled:', km_travelled)
    print('Chocolate bars in food pack:', chocolate_bars)
    print('The empire is ', km_travelled - enemy_distance, 'km away from you.')
    print()
    time.sleep(2)
    user_choice = menu()

    if hunger > 4:
        print('You are hungry')
    elif hunger > 6:
        print('You are dead.')
        done = True

    chance = random.randint(1,21)
    if chance == 20:
        print('You found a rebel encampment! You and your wompa rest, and you refill your food.')
        hunger = 0
        wompa_tiredness = 0
        chocolate_bars = 3

    chance = 0

    if wompa_tiredness > 5:
        print('Your wompa is getting tired.')
    elif wompa_tiredness > 8:
        print('Your wompa is dead. You die of hunger.')
        print('Your wompa is dead. You die of hunger.')
        done = True

    if enemy_distance >= km_travelled - 15:
        print('Your enemies are getting close')
    if enemy_distance >= km_travelled:
        print('You are captured.')
        done = True

    if km_travelled >= 200:
        print('You win!!!')
        done = True

    if user_choice == 'a':
        if chocolate_bars != 0:
            chocolate_bars -= 1
            hunger = 0
            enemy_distance += random.randint(7, 15)
            print('You now have',chocolate_bars,'chocolate bars.')
            if chocolate_bars == 0:
                print('You have no chocolate bars.')

    elif user_choice == 'b':
        km_travelled += random.randint(5,15)
        wompa_tiredness += 1
        hunger += 1
        enemy_distance += random.randint(7,15)

    elif user_choice == 'c':
        km_travelled += random.randint(10,21)
        wompa_tiredness += random.randint(1,4)
        hunger += 1
        enemy_distance += random.randint(7,15)

    elif user_choice == 'd':
        wompa_tiredness == 0
        enemy_distance += random.randint(1,15)
        print('Your wompa is happy with you.')

    elif user_choice == 'q':
        print('You have quit the game.')
        done = True


