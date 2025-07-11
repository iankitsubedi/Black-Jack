import random

cards = {
    "Ace": [1,11],
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

a = input("Do you want to play black jack(Y/N): ").lower()
z = "y"

while(z != "n"):
    my_card = []
    com_card = []
    # random choice for the user
    if(z == "y"):
        x = random.choice(list(cards.keys()))
        y = random.choice(list(cards.keys()))
        my_card.extend([x,y])
        # Use calculate_hand_value instead of get_card_value sum as I can do both in the function() i.e Ace
        # and the normal card
        nosum = calculate_hand_value(my_card)
        print("Your cards: "+f"[{x} , {y}]"+f",  current score: {nosum}")

        #random choice for the computer
        com1 = random.choice(list(cards.keys()))
        com_card.extend([com1])
        comsum = calculate_hand_value(com_card)
        print(f"Computer's first card: {com_card[0]}")

        while nosum < 21 and comsum < 21: 
            if(a == "y"):
                #checking starts
                check = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if(check == "y"):
                    z = random.choice(list(cards.keys()))
                    my_card.extend([z])
                    # again calculate total hand value
                    nosum = calculate_hand_value(my_card)
                    if(nosum < 21):
                        print(f"Your  hand is {my_card},current score = {nosum}")
                        print(f"Computer  hand is {com_card},current score = {comsum}")
                    elif(nosum == 21):
                        print(f"Your  hand is {my_card},current score = {nosum}")
                        print(f"Computer  hand is {com_card},current score = {comsum}")
                        print("You won")

                    else:
                        print(f"Your final hand is {my_card},final score = {nosum}")
                        print(f"Computer  hand is {com_card},final score = {comsum}")
                        print("You lose")

                else:
                    computer = random.choice(list(cards.keys()))
                    com_card.extend([computer])
                    comsum = calculate_hand_value(com_card)
                    while comsum < 21:
                        computer = random.choice(list(cards.keys()))
                        com_card.extend([computer])
                        comsum = calculate_hand_value(com_card)

                    print(f"Your final hand is {my_card},final score = {nosum}")
                    print(f"Computer  hand is {com_card},final score = {comsum}")
                    if(comsum == 21):
                        print("You lose")
                    else:
                        print("You won")

    print("\n")    
    z = input("Do you want to continue for the next round(Y/N): ").lower()
