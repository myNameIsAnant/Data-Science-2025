import random

chosennos = random.randint(1,101)
# print(chosennos)

"""
def usrpick(start,end):
    return int(input(f"Choose a number b/w {start} to {end}: "))
"""

def guessGame():
    usrchoice = []
    low = 1
    high = 100
    for i in range(1,6):
        userchoice = int(input(f"Attempt {i} of 5 - Choose a number b/w {low} to {high}: "))
        if userchoice == chosennos:
            return f"Great Your Chosen Number {userchoice} matches with Computer {chosennos}. You Won!!!"
        elif userchoice < chosennos:
            if i < 5:
                print(f"Attempt {i} of 5 failed. Hint: Try Higher Number")
                low = userchoice + 1
            usrchoice.append(userchoice)
        else:
            if i < 5:
                print(f"Attempt {i} of 5 failed. Hint: Try Lower Number")
                high = userchoice - 1
            usrchoice.append(userchoice)
    
    return f"You Lost!!! Your weren't able to guess the Chosen Number {chosennos}. You guessed {usrchoice}. Try Again!!!"

print(guessGame())


