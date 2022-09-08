"""EX02 One Shot Worlde!"""
__author__ = "730560264"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
display = ""
# declares the colored boxes for correct/ incorrect boxes
i: int = 0

while i < len(secret):
    if len(guess) != len(secret):
        guess = input(f"That was not {len(secret)} letters! Try again: ")
        # ensures that guess is as long as the secret, if not try again
    elif guess[i] == secret[i]:
        display = display + GREEN_BOX 
    elif guess[i] != secret[i]:
        j = 0
        functiontype = "False"
        # if the index of the guess is not the same as the secret then it goes into the while loop
        while j < len(secret):
            if guess[i] == secret[j]:
                functiontype = "True"
            j += 1
        if functiontype == "True":
            display = display + YELLOW_BOX
        else:
            display = display + WHITE_BOX
        # sets up the index comparisons and the corresponding colored boxes
    i += 1


if len(guess) == len(secret):
    if guess == secret:
        print(display)
        print("Woo! You got it!")
        # if the guess is the secret then "Woo! You got it!" would appear
    elif guess != secret:
        print(display)
        print("Not quite. Play again soon!")
        # else if the guess is not the secret then "Not quite. Play again soon!" would appear