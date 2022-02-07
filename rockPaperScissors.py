import random
from re import S


# creating my first game
##
def gameWin(comp, you):
    win = None
    gameValid = False
    b = [win, gameValid]
    if you in {'r', 'p', 's'} :
        
        if comp == you:
            print("Game Tied!!!")
        elif comp == 'r':
            if you == 'p':
             win = True
            elif you == 's':
                win = False
        elif comp == 'p':
            if you == 's':
                win = True
            elif you == 'r':
                win = False
        elif comp == 's':
            if you == 'r':
                win = True
            elif you == 'p':
                win = False
        return b
    else:
        gameValid = False
        print("invalid choice!")
        return b


game = True
print("Computer's Turn : Rock(R), Paper(P) or Scissors(S) ?")
n = random.randint(1, 3)
if n == 1:
    comp = 'r'
elif n == 2:
    comp = 'p'
else:
    comp = 's'


print("Computer has chosen...")
you = input("Your Turn : Rock(R), Paper(P) or Scissors(S) (Exit : e) ?")

print("You have chosen...Brace Yourself!!!!")

b = gameWin(comp, you)
win = b[0]
gameValid = b[1]

if gameValid:
    if win :
        print("You Win!!!!")
    else:
        print("You Lose :( ")
