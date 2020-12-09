import random


# Assign zero to score of two players.
player1_score = 0
player2_score = 0
total_dice_rolls = 5
player1_dicerolls = 0
player2_dicerolls = 0


# This functions rolls dice whenever it is called.
def roll_dice():
    dice = random.randint(1, 6)
    return dice


print("1 - player1")
print("2 - player2")
print("E or e - exit the game")
print("\n")

print("              ***   Game rules    ***")
print("1. Player1 and Player2 should roll the dice alternatively.")
print("2. Any player can roll the dice only 5 times.")
print("3. Player with maximum score wins the game.\n")

while player1_dicerolls < total_dice_rolls or player2_dicerolls < total_dice_rolls:
    op = input("Enter your option(1, 2, e): ")

    if op == "1":
        rolled = roll_dice()
        print("rolled dice side = ", rolled)
        player1_score += rolled
        player1_dicerolls = player1_dicerolls + 1
        print("You have rolled ", player1_dicerolls, " times.\n")
        # print("*___________________SCORE BOARD___________*")
        # print("|\tPlayer1 = ", player1_score, "\t\t\t Player2 = ", player2_score, "|")
        # print("*-----------------------------------------*")

    elif op == "2":
        rolled = roll_dice()
        print("rolled dice side = ", rolled)
        player2_score += rolled
        player2_dicerolls = player2_dicerolls + 1
        print("You have rolled ", player2_dicerolls, " times.\n")
        print("*___________________SCORE BOARD___________*")
        print("|\tPlayer1 = ", player1_score, "\t\t\t Player2 = ", player2_score, "|")
        print("*-----------------------------------------*")
        print("\n")

    elif op == "e" or "exit" or "Exit":
        break
    else:
        print("Invalid input")

if player2_score < player1_score:
    print("Player1 wins!")
    print("   PLAYER1 ")
    print("   _______ ")
    print("  |   1   |  ")
    print("--         --")
elif player1_score < player2_score:
    print("Player2 wins!")
    print("   PLAYER2 ")
    print("   _______ ")
    print("  |   1   |  ")
    print("--         --")
else:
    print("Game drawn")


print("\n")
print("You win. Thank you for playing my game.")
