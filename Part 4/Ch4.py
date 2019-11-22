#Jack Carlson
import random
random_number = random.randint(15,26)
guess = 0
while guess != random_number:
    guess = int(input('What is the random number between 15 and 25'))
    if guess < random_number:
        print('Too low!')
    elif guess > random_number:
        print('Too high!')
    if guess == random_number:
        print("Congrats! The random number was", random_number,'!')
########################################################################################################################
user_choice = 0
done = False
while done != True:
    user_choice = (input('Do you choose rock, paper, or scissors.'))
    if user_choice.lower() == 'rock':
        print('You chose rock.')
    elif user_choice.lower() == 'paper':
        print('You chose paper.')
    elif user_choice.lower() == 'scissors':
        print('You chose scissors.')
    computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        print('The computer chose rock.')
    elif computer_choice == 2:
        print('The computer chose paper.')
    elif computer_choice == 3:
        print('The computer chose scissors.')

    if user_choice == 'rock' and computer_choice == 3:
        print('You won.')
    elif user_choice == 'rock' and computer_choice == 2:
        print('You lost.')
    elif user_choice == 'rock' and computer_choice == 1:
        print('It was a draw.')

    if user_choice == 'paper' and computer_choice == 1:
        print('You won.')
    elif user_choice == 'paper' and computer_choice == 3:
        print('You lost.')
    elif user_choice == 'paper' and computer_choice == 2:
        print('It was a draw.')

    if user_choice == 'scissors' and computer_choice == 2:
        print('You won.')
    elif user_choice == 'scissors' and computer_choice == 1:
        print('You lost.')
    elif user_choice == 'scissors' and computer_choice == 3:
        print('It was a draw.')

    quit = input("Do you want to quit? ")
    if quit == 'yes':
        done = True
    else:
        done = False

