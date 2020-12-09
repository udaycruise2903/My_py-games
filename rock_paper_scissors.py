import random

pc = " "
cc = " "

pp = 0         # player1_points
cp = 0         # computer_points
p1_chance = 0
c_chance = 0
total_chances = 3

game_list = ["ROCK", "SCISSORS", "PAPER"]


def play():
    rch = random.choice(game_list)
    return rch

print("\t------------------  WELCOME ----------------------\n")
print("\t\t\t\t   /\    \   /   |-----  | ")
print("\t\t\t\t  /00\    \*/    | @#$%8 | ")
print("\t\t\t\t /0000\ **   **  |_______| \n")

player1 = str(input("Enter your name: "))

print("\nType any of the following -\nROCK\tPAPER\tSCISSORS\tE - exit the game.")
print("\n")

while p1_chance < total_chances or c_chance < total_chances:
    pc = str.upper((input("Enter your choice: ")))
    '''
    op = int(input("Enter your choice: "))
    if op == "1":
        pc = "ROCK"
    elif op == "2":
        pc = "PAPER"
    elif op == "3":
        pc = "SCISSORS"
    else:
        print("Invalid input")'''
    p1_chance = p1_chance + 1
    print(player1, " chose ", pc, ". Your chances = ", (total_chances-p1_chance))

    cc = play()
    c_chance = c_chance + 1
    print("Computer chose ", cc, ". It has ", (total_chances-c_chance), " chances.")

    if pc == "ROCK" and cc == "ROCK":
        pass
    elif pc == "ROCK" and cc == "SCISSORS":
        pp = pp + int(1)
    elif pc == "ROCK" and cc == "PAPER":
        cp = cp + int(1)
    elif pc == "SCISSORS" and cc == "ROCK":
        cp = cp + int(1)
    elif pc == "SCISSORS" and cc == "SCISSORS":
        pass
    elif pc == "SCISSORS" and cc == "PAPER":
        pp = pp + int(1)
    elif pc == "PAPER" and cc == "ROCK":
        pp = pp + int(1)
    elif pc == "PAPER" and cc == "PAPER":
        pass
    elif pc == "PAPER" and cc == "SCISSORS":
        cp = cp + int(1)
    else:
        break

    print("\n")
    print("*___________________SCORE BOARD___________*")
    print("|\t", player1, " = ", pp, "\t\t\t Computer = ", cp, "|")
    print("*-----------------------------------------*")
    print("\n")

if cp < pp:
    print(player1, " wins!")
elif pp < cp:
    print("Computer wins!")
else:
    print("Game Drawn")

print("\nThank you for playing my game.")
