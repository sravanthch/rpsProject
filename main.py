import random
while True:
    choices=['rock','paper','scissors']
    computer = random.choice(choices)
    player=None
    while player not in choices:
        player=input("\nrock, paper or scissors??").lower()
    if player==computer:
        print('Computer:', computer)
        print('Player:', player)
        print("Tie!!")
    elif computer=='rock':
        if player=='paper':
            print('Computer:',computer)
            print('Player:',player)
            print("You Win")
        if player=='scissors':
            print('Computer:', computer)
            print('Player:', player)
            print("You lose")
    elif computer=='paper':
        if player=='rock':
            print('Computer:',computer)
            print('Player:',player)
            print("You lose")
        if player=='scissors':
            print('Computer:', computer)
            print('Player:', player)
            print("You Win")
    elif computer=='scissors':
        if player=='rock':
            print('Computer:',computer)
            print('Player:',player)
            print("You Win")
        if player=='paper':
            print('Computer:', computer)
            print('Player:', player)
            print("You lose")
    play_again=input("\n\nPLAY AGAIN??(Yes/No)").lower()
    if play_again!='yes':
        break
print("Bye!!")




