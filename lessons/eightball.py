from random import randint, random

questions: str = input("Ask a yes/no question...")
response: int = randint(0 , 2)

if response == 0:
    print("Yes, definitely")
elif response == 1:
    print("Ask again later")
elif response == 2:
    print("You betcha")
else: 
    print("My source say no")