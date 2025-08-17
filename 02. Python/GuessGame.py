import random

chosennos = random.randint(1,101)
# print(chosennos)

"""
def usrpick(start,end):
    return int(input(f"Choose a number b/w {start} to {end}: "))
"""

def guessGame():
    usrchoice = []
    for i in range(1,6):
        userchoice = int(input("Choose a number b/w 1 to 100: "))
        if userchoice == chosennos:
            return f"Great Your Chosen Number {userchoice} matches with Computer {chosennos}. You Won!!!"
        elif userchoice < chosennos:
            if i < 5:
                print(f"Attempt {i} of 5 failed. Hint: Try Higher Number")
            usrchoice.append(userchoice)
        else:
            if i < 5:
                print(f"Attempt {i} of 5 failed. Hint: Try Lower Number")
            usrchoice.append(userchoice)
    
    return f"You Lost!!! Your weren't able to guess the Chosen Number {chosennos}. You guessed {usrchoice}. Try Again!!!"

print(guessGame())    


