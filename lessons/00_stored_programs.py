user_input=input("Choose a number between 1 and 5: ")
import random
random=random.randint(1,5)
if int(user_input)==int(random):
    print("Congrats you guessed the right number!!!")
else:
    print("Wrong, the random number was " + str(random))
