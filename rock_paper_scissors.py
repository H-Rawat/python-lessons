import random

choices = ['rock', 'paper', 'scissors']

computer = random.choice(choices)
player = None

while player not in choices:
    player = input('rock, paper, or scissors?: ').lower()

while True:
    if player == computer:
        print("computer:", computer)
        print("player:", player)
        print("TIE")
    elif player == 'rock':
        if computer == 'paper':
            print("computer:", computer)
            print("player:", player)
            print("YOU LOST")
        if computer == 'scissors':
            print("computer:", computer)
            print("player:", player)
            print("YOU WON")
    elif player == 'paper':
        if computer == 'rock':
            print("computer:", computer)
            print("player:", player)
            print("YOU WON")
        if computer == 'scissors':
            print("computer:", computer)
            print("player:", player)
            print("YOU LOST")
    elif player == 'scissors':
        if computer == 'paper':
            print("computer:", computer)
            print("player:", player)
            print("YOU WON")
        if computer == 'rock':
            print("computer:", computer)
            print("player:", player)
            print("YOU LOST")
    play_again = input('Play again?: Yes or No: ').lower()
    if play_again != 'yes':
        break

print("Thanks for playing the gam")
