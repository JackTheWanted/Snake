#Jack C
capital = input('What is the capital of Russia?')
score = 0
if capital.lower()=='moscow':
    score += 1
    print('Correct, very nice!')
elif capital.lower()=='kiev' or capital.lower()=='st petersburg':
    print('Well that is kinda close I guess.')
else:
    print('Wrong, you idiot.')
between = float(input('What is a number between 1 and 10?'))
if between <= 10 and between >= 1:
    score += 1
    print('Good job! You can do basic math!')
else:
    print('How did you get that wrong? Are you stupid?')
print('Who is the current CEO of youtube?')
print('A: Steve Jobs')
print('B: Susan Wojcicki')
print('C: Gavrilo Princip')
print('D: Joseph Stalin')
ceo = input()
if ceo.lower() == 'b':
    score += 1
    print('Correct! Good job.')
elif ceo.lower() == 'a':
    print('Maybe you\'re thinking of Apple? Steve Jobs has been dead for years!')
elif ceo.lower() == 'c':
    print('Gavrilo Princip started WW1, he is so far from the correct answer it hurts.')
elif ceo.lower() == 'd':
    print('Joseph Stalin is famous for something much worse than youtube, read a book.')
else:
    print('You didn\'t even pick one of the 4 options')
moon = input('True or False: Russia\'s area is roughly the same as the surface area of the moon.')
if moon.lower() == 'false':
    score += 1
    print('The moon\'s surface area is almost twice that of Russia, Russia\'s is much closer to Pluto\s surface area.')
elif moon.lower() == 'f':
    score += 1
    print('The moon\'s surface area is almost twice that of Russia, Russia\'s is much closer to Pluto\s surface area.')
elif moon.lower() == 'true':
    print('The moon is much bigger than you think it is, their sizes aren\'t even close.')
elif moon.lower() == 't':
    print('The moon is much bigger than you think it is, their sizes aren\'t even close.')
equals = int(input('What is 2*8+4?'))
if equals == 20:
    score += 1
    print('Good job! That\'s like Grade 5 math!')
elif equals <= 19 and equals >=17:
    print('I mean I guess it\'s close, but this was easy math.')
elif equals >= 21 and equals <= 23:
    print('I mean I guess it\'s close, but this was easy math.')
else:
    print('What\'s wrong with you? Did you even pass Grade 5 math?')
print('Congrats, you got',score, ' answers right.')
result = (score/5)*100
print('That\' a score of',result,' percent.')
if result == 100:
    print('Incredible! You got perfect!')
elif result == 0:
    print('How did you manage to not get a single answer right?')

