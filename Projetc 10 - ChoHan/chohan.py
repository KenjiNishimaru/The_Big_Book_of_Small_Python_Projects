import os,random

print('''In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total is even or odd (cho or han) number.
''')
money= 5000
japanese_number = {1:'Iti',2:'Ni',3:'San',4:'Yon',5:'Go',6:'Roku'}

while True:
    if money == 0:
        print('You have 0 mon left, thanks for playing!')
        os._exit(0)
    print(f'You have {money} mon. How much do you bet? (or QUIT)')
    while True:
        bet = input('> ')
        if bet.isdigit():
            bet = int(bet)
            if bet > money:
                print('You dont have that much money, choose a valid amount')
                continue
            money -= bet
            break
        else:
            bet = bet.upper()
            if bet == 'QUIT':
                print('Thanks for playing!')
                os._exit(0)
            else:
                print('Invalid input. Please enter your bet or QUIT')
                continue

    print('''The dealer swirls the cup and you hear the rattle of dice.
    The dealer slams the cup on the floor, still covering the
    dice and asks for your bet.

        CHO (even) or HAN (odd)?
    ''')

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    odd = (dice1 + dice2) % 2 == 1
    while True:
        choice = input('> ').upper()
        if choice not in ['ODD','EVEN','HAN','CHO']:
            print('Please enter either "CHO" or "HAN"')
            continue
        break

    print('The dealer lifts the cup to reveal:')
    if (choice in ['ODD','HAN'] and odd) or (choice in ['EVEN','CHO'] and not odd):
        print(f'{japanese_number[dice1]} - {japanese_number[dice2]}')
        print(f'{dice1} - {dice2}')
        print(f'You won! You take {2*bet} mon.')
        print(f'The house collects a {int(bet/10)} mon fee.')
        money += (2*bet) - int(bet/10)
    else:
        print(f'{japanese_number[dice1]} - {japanese_number[dice2]}')
        print(f'{dice1} - {dice2}')
        print('You lose!')

