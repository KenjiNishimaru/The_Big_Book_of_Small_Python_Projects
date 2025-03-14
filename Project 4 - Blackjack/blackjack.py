import os, random

def new_game():
    dealer_cards = [[], [], [], []]
    player_cards = [[], [], [], []]
    dealer = player = 0
    deck = init_deck()
    return True,dealer_cards, player_cards, dealer, player, deck

def init_deck():
    new_deck = [
        ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
        ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
        ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
        ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
    ]
    return new_deck

def take_card(deck, player_deck):
    suit = random.randint(0, 3)
    card = random.randint(0, 11)

    while deck[suit][card] == 0:  ## A carta já tinha sido removida do baralho
        suit = random.randint(0, 3)
        card = random.randint(0, 12)
    player_deck[suit].append(deck[suit][card])
    deck[suit][card] = 0

    return suit, card, deck

def sum_score(card, score):
    if card == 0:
        if score <= 10:
            score += 11
        else:
            score += 1
    elif card == 10 or card == 11 or card == 12:
        score += 10
    else:
        score += card + 1
    return score

def printCard(player_cards, player, score):
    deck = {0: "\u2660", 1: "\u2665", 2: "\u2666", 3: "\u2663"} # suits from Unicode
    print(f"{player}: {score}")
    for suit in range(4):
        for card in player_cards[suit]:
            print(f" ___", end="  ")
    print()

    for suit in range(4):
        for card in player_cards[suit]:
            if card == 10:
                print(f"|{card} |", end=" ")
            else:
                print(f"|{card}  |", end=" ")
    print()

    for suit in range(4):
        for card in player_cards[suit]:
            print(f"| {deck[suit]} |", end=" ")
    print()

    for suit in range(4):
        for card in player_cards[suit]:
            if card == 10:
                print(f"|_{card}|", end=" ")
            else:
                print(f"|__{card}|", end=" ")
    print()
    print()

print("Rules:")
print("Try to get as close to 21 without going over.")
print("Kings, Queens, and Jacks are worth 10 points.")
print("Aces are worth 1 or 11 points.")
print("Caras 2 through 10 are worth their face value.")
print("(H)it to take another card.")
print("(S)tand to stop taking cards.")
print("On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.")
print("In case of a tie, the bet is returned to the player.")
print("The dealer stops hitting at 17.")

available_money = 5000  # Starting Money
FirstHand,dealer_cards, player_cards, dealer, player, deck = new_game()

while True:
    print(f"Money: {available_money}")
    if available_money <= 0:
        bet = "QUIT"
    else:
        print(f"How much do you bet? (1-{available_money}, or QUIT)")
        bet = input("> ")

    if bet.upper() == "QUIT":
        print("Thanks for playing")
        os._exit(0)
    else:
        try:
            bet = int(bet)
            try:
                if bet > available_money:
                    raise ValueError(
                        "You dont have that much money. Enter a valid quantity.\n"
                    )
            except ValueError as e:
                print(e)
                continue
        except:
            print("Invalid input. Enter an amount of money or 'QUIT'.\n")
            continue
    available_money -= bet
    print(f"Bet: {bet}\n")

    suit, card, deck = take_card(deck, dealer_cards)
    dealer = sum_score(card, dealer)
    suit, card, deck = take_card(deck, dealer_cards)
    dealer = sum_score(card, dealer)

    suit, card, deck = take_card(deck, player_cards)
    player = sum_score(card, player)
    suit, card, deck = take_card(deck, player_cards)
    player = sum_score(card, player)

    printCard(dealer_cards, "DEALER", dealer)
    printCard(player_cards, "PLAYER", player)

    while True:
        if FirstHand:
            print("(H)it, (S)tand, (D)ouble down")
        else:
            print("(H)it, (S)tand")
        option = input("> ")
        option = option.upper()
        if option not in ["H", "S", "D"]:
            print("Invalid input, hit 'h', 's' or 'd' instead.")
            sys.exit(0)
        if (option == "D" and FirstHand) or option == "H":
            suit, card, deck = take_card(deck, player_cards)
            player = sum_score(card, player)
        if option == "D" and FirstHand:
            if available_money >= bet:
                available_money -= bet
                bet += bet
            else:
                print('You dont have that much money. We will keep the initial bet')
        if dealer < 17:
            suit, card, deck = take_card(deck, dealer_cards)
            dealer = sum_score(card, dealer)
        printCard(dealer_cards, "DEALER", dealer)
        printCard(player_cards, "PLAYER", player)

        FirstHand = False

        if option == "S":
            while dealer < 17:
                suit, card, deck = take_card(deck, dealer_cards)
                dealer = sum_score(card, dealer)
                printCard(dealer_cards, "DEALER", dealer)
                printCard(player_cards, "PLAYER", player)
            break
        if player >= 21 or dealer >= 21:
            break

    if player == dealer or (player>21 and dealer>21):
        print("It's a tie. Your money is returned.")
        available_money += bet
        FirstHand,dealer_cards, player_cards, dealer, player, deck = new_game()

    elif player > 21 or (dealer>player and dealer <= 21):
        print(f"You lost ${bet}")
        FirstHand,dealer_cards, player_cards, dealer, player, deck = new_game()

    elif player == 21 or dealer > 21 or player>dealer:
        print(f"You won ${bet}")
        available_money += 2 * bet
        FirstHand,dealer_cards, player_cards, dealer, player, deck = new_game()






