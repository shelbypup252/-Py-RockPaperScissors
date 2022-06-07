import random

def welcome():
    print('Welcome to Rock Paper Scissors!')
    print('--------------------------------')
    
    
def determineMenuOption():
    print("Which option do you choose?")
    print('(1): Rock')
    print('(2): Paper')
    print('(3): Scissors')
    print('--------------------------------')
    menuoption = int(input('Please choose a menu option (1-3): '))
    
    while (not(menuoption >= 1 and menuoption <= 3) ):
        print("That's not a valid menu option!")
        menuoption = int(input('Please choose a menu option (1-3): '))
    
    return menuoption


def rollValue():
    roll = int(random.randrange(1, 3))
    return roll
    
    
def determinerOfWin(menuRPS, roll):
    won = int(0)
    if (menuRPS == 1 and roll == 3):
        won = int(1)
    if (menuRPS == 2 and roll == 1):
        won = int(2)
    if (menuRPS == 3 and roll == 2):
        won = int(3)
    if (menuRPS == 3 and roll == 1):
        won = int(4)
    if (menuRPS == 1 and roll == 2):
        won = int(5)
    if (menuRPS == 2 and roll == 3):
        won = int(6)
    
    return won





def playAgainMessage():
    print('')
    print("Would you like to play again?")
    print("-------------------------------")
    
    
def playAgainf():
    print("(1): Yes")
    print("(2): No")
    print("-------------------------------")
    menuoption = int(input('Please choose a menu option (1-2): '))
    
    while (not(menuoption >= 1 and menuoption <= 2) ):
        print("That's not a valid menu option!")
        menuoption = int(input('Please choose a menu option (1-2): '))
    
    print("-------------------------------")
    return menuoption
    

def report(wins, losses):
    netWinLoss = int(wins - losses)
    
    print('')
    print("Report:")
    print("-------------------------------")
    print("Wins: ", wins)
    print("Losses: ", losses)
    print("Net wins/losses: ", netWinLoss)
    
    if (netWinLoss > 0):
        print('Well done! You win overall!')
    if (netWinLoss < 0):
        print("Too bad! You lose overall!")
    if (netWinLoss == 0):
        print("Your wins and losses tied!")
    
    print("-------------------------------")
    print("Thank you for playing!")
    print('')



    
welcome()
    
menuRPS = int(determineMenuOption())
roll = int(rollValue())

wonRoundFlag = int(determinerOfWin(menuRPS, roll))

wins = int(0)
losses = int(0)
    
if (wonRoundFlag == 1):
    print("Rock beats scissors!")
    print("You won! (+1 win)")
    wins = wins + 1
    
if (wonRoundFlag == 2):
    print("Paper covers rock!")
    print("You won! (+1 win)")
    wins = wins + 1

if (wonRoundFlag == 3):
    print("Scissors cut paper!")
    print("You won! (+1 win)")
    wins = wins + 1    

if (wonRoundFlag == 4):
    print("Rock beats scissors!")
    print("You lost! (+1 loss)")
    losses = losses + 1
    
if (wonRoundFlag == 5):
    print("Paper covers rock!")
    print("You lost! (+1 loss)")
    losses = losses + 1

if (wonRoundFlag == 6):
    print("Scissors cut paper!")
    print("You lost! (+1 loss)")
    losses = losses + 1
    

playAgainMessage()

playAgain = int(playAgainf())

while (playAgain == 1):
    
    wonRoundFlag = int(0)
    playAgain = int(0)
    menuRPS = determineMenuOption()
    roll = rollValue()

    wonRoundFlag = int(determinerOfWin(menuRPS, roll))

    print('')
    if (wonRoundFlag == 1):
        print("Rock beats scissors!")
        print("You won! (+1 win)")
        wins = wins + 1
        
    if (wonRoundFlag == 2):
        print("Paper covers rock!")
        print("You won! (+1 win)")
        wins = wins + 1

    if (wonRoundFlag == 3):
        print("Scissors cut paper!")
        print("You won! (+1 win)")
        wins = wins + 1    

    if (wonRoundFlag == 4):
        print("Rock beats scissors!")
        print("You lost! (+1 loss)")
        losses = losses + 1
        
    if (wonRoundFlag == 5):
        print("Paper covers rock!")
        print("You lost! (+1 loss)")
        losses = losses + 1

    if (wonRoundFlag == 6):
        print("Scissors cut paper!")
        print("You lost! (+1 loss)")
        losses = losses + 1

    playAgainMessage()

    playAgain = int(playAgainf())
    

if (playAgain == 2):
    report(wins, losses)
    