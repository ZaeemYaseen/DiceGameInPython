import random

def main():
    player1 = input("Enter player1 name: ")
    player2 = input("Enter player2 name: ")

    print("\nHello " + player1)
    print("Hello " + player2)

    p1 = 0
    winsPlayer1 = 0
    p2 = 0
    winsPlayer2 = 0
    rounds = 1
    while rounds != 4:
        print("\nRound = " + str(rounds))
        p1 = roll_dice()
        p2 = roll_dice()
        print(player1 + " Rolls " + str(p1))
        print(player2 + " Rolls " + str(p2))

        if (p1>p2):
            winsPlayer1 = winsPlayer1 + 1
            print(player1 + " wins! \n")
        elif(p2>p1):
            winsPlayer2 = winsPlayer2 + 1
            print(player2 + " wins! \n")
        else:
            print("Draw! \n")
        
        rounds = rounds + 1
    
    if winsPlayer1 > winsPlayer2:
        print(player1 + " Wins - Rounds Won : " + str(winsPlayer1))
    elif (winsPlayer2 > winsPlayer1):
        print(player2 + " Wins - Rounds Won : " + str(winsPlayer2))
    else:
        print("Draw!")

def roll_dice():
    dice = random.randint(1,6)
    return dice

main()
