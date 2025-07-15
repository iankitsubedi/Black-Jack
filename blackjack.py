import random

cards = {
    "Ace": [1, 11],
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}

def calculate_hand_value(hand):
    total = 0
    ace_count = 0
    for card in hand:
        if card == "Ace":
            ace_count += 1
        else:
            total += cards[card]
    for _ in range(ace_count):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    return total

z = input("Do you want to play Blackjack (Y/N): ").lower()

while z != "n":
    my_card = []
    com_card = []

    if z == "y":
        x = random.choice(list(cards.keys()))
        y = random.choice(list(cards.keys()))
        my_card.extend([x, y])
        nosum = calculate_hand_value(my_card)
        print(f"Your cards: [{x}, {y}], current score: {nosum}")

        com1 = random.choice(list(cards.keys()))
        com_card.append(com1)
        comsum = calculate_hand_value(com_card)
        print(f"Computer's first card: {com_card[0]}")

        # Player's turn
        while True:
            if nosum >= 21:
                break

            check = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if check == "y":
                z = random.choice(list(cards.keys()))
                my_card.append(z)
                nosum = calculate_hand_value(my_card)

                print(f"Your hand is {my_card}, current score = {nosum}")
                print(f"Computer hand is {com_card}, current score = {comsum}")

                if nosum > 21:
                    print("You went over 21. You lose.")
                    break
                elif nosum == 21:
                    print("You hit 21!")
                    break
            else:
                break

        # Computer's turn (only if player hasn't busted)
        if nosum <= 21:
            while comsum < 17 or (comsum < nosum and comsum < 21):
                computer = random.choice(list(cards.keys()))
                com_card.append(computer)
                comsum = calculate_hand_value(com_card)

            print(f"Your final hand: {my_card}, final score = {nosum}")
            print(f"Computer final hand: {com_card}, final score = {comsum}")

            if comsum > 21:
                print("Computer went over 21. You win!")
            elif comsum == nosum:
                print("It's a draw!")
            elif comsum > nosum:
                print("Computer wins!")
            else:
                print("You win!")

    print("\n")
    z = input("Do you want to continue for the next round (Y/N): ").lower()

print("Thanks for playing!")
