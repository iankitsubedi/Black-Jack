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
def get_card_value(card):
    if card == "Ace":
        return random.choice([1, 11])
    else:
        return cards[card]

a = input("Do you want to play black jack(Y/N):").lower()
n = ""
while(n != "n"): 
    if(a == "y"):
        my_card = []
        com_card = []

        # random choice for the user
        x = random.choice(list(cards.keys()))
        y = random.choice(list(cards.keys()))
        my_card.extend([x,y])
        nosum = get_card_value(x) + get_card_value(y)
        print("Your cards: "+f"[{x} , {y}]"+f",  current score: {nosum}")

        #random choice for the computer
        com1 = random.choice(list(cards.keys()))
        com2 = random.choice(list(cards.keys()))
        com_card.extend([com1,com2])
        comsum = get_card_value(com1) + get_card_value(com2)
        print(f"Computer's first card: {com_card[0]}")

        #checking starts
        check = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if(check != y):
            z = random.choice(list(cards.keys()))
            my_card.extend([z])
            nosum = nosum + get_card_value(z)
            if(nosum <= 21):
                print(f"Your  hand is {my_card},current score = {nosum}")
                print(f"Computer  hand is {com_card},current score = {comsum}")

            else:
                print(f"Your final hand is {my_card},final score = {nosum}")
                print(f"Computer  hand is {com_card},final score = {comsum}")
                print("You lose")

        else:
                computer = random.choice(list(cards.keys()))
                com_card.extend([computer])
                comsum = comsum + get_card_value(computer)
                while(comsum >= 21):
                    if(comsum < 21):
                        computer = random.choice(list(cards.keys()))
                        com_card.extend([computer])
                        comsum = comsum + get_card_value(computer)
                
                print(f"Your final hand is {my_card},final score = {nosum}")
                print(f"Computer  hand is {com_card},final score = {comsum}")
                if(comsum == 21):
                    print("The computer won.")
    n = input("Do you want to continue for the next round(Y/N): ").lower()

    