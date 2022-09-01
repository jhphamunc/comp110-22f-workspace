"""EX02 One Shot Worlde!"""
__author__ = "730560264"

secret: str = "python"
guess: str = input("What is your " + str(len(secret)) + "-letter guess: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
display = ""

i: int = 0

while i < 6:
    if len(guess) != len(secret):
        guess = input("That was not " + str(len(secret)) + " letters! Try again: ")
    elif guess[i] == secret[i]:
        display = display + GREEN_BOX 
    elif guess[i] != secret[i]:
        j = 0
        functiontype = "False"
        while j < 6:
            if guess[i] == secret[j]:
                functiontype = "True"
            j += 1
        if functiontype == "True":
            display = display + YELLOW_BOX
        else:
            display = display + WHITE_BOX
    i += 1

while guess != "":
    if len(guess) == len(secret):
        if guess == secret:
            print(display)
            print("Woo! You got it!")
            exit()
        elif guess != secret:
            print(display)
            print("Not quite. Play again soon!")
            exit()