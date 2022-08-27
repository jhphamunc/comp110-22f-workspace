"""This is a Docstring."""

__author__ = "730560264"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 letters.")
    quit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    quit()

print("Searching for " + single_character + " in " + five_character_word)

count = 0
plural = ""

if five_character_word[0] == single_character:
    print(single_character + " found at index 0")
    count = count + 1 
if five_character_word[1] == single_character:
    print(single_character + " found at index 1")
    count = count + 1 
if five_character_word[2] == single_character:
    print(single_character + " found at index 2")
    count = count + 1 
if five_character_word[3] == single_character:
    print(single_character + " found at index 3")
    count = count + 1 
if five_character_word[4] == single_character:
    print(single_character + " found at index 4")
    count = count + 1 

if count > 1:
    plural: str = "s"

print(str(count) + " instance" + plural + " of " + single_character + " found in " + five_character_word)
if count == 0:
    print("No instances of " + single_character + " found in " + five_character_word)

exit()