import random

digits = 3
max_guesses = 10
guess = 0 #number of guesses by the player
gamerunning = 1 #flag to decide if its over before max guesses (player got the right answer within 10 guesses)

random_number = random.randint(100,999)
random_string = str(random_number)

print("Bagels, a deductive logic game.")
print(f'I am thinking of a {digits}-digit number. Try to guess what it is.')
print('Here are some clues:\nWhen I say:\tThat means:')
print(' Pico\t\tOne digit is correct but in the wrong position.')
print(' Fermi\t\tOne digit is correct and in the right position.')
print(' Bagels\t\tNo digit is correct')
print('I have thought up a number.')
print(f'You have {max_guesses} guesses to get it.')

while(guess < max_guesses and gamerunning):
    Bagels = 1
    print(f'> Guess #{guess}:')
    number_guessed= input()
    while(len(number_guessed) != digits):
        print(f'Number guessed must have {digits} digits')
        number_guessed= input()

    if(number_guessed == random_string):
        gamerunning = 0
        break

    for i in range(digits):
        if(number_guessed[i] in random_string):
            Bagels = 0
            if(number_guessed[i] == random_string[i]):
                print('Fermi')
            else:
                print('Pico')

    if Bagels == 1:
        print('Bagels')

    guess +=1 # number of current guess

if(gamerunning == 1):
    print(f'You didnt get it in {max_guesses} guesses.')
else:
    print('You got it!')
