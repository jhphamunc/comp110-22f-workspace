"""This is a Docstring."""

__author__ = "730560264"

five_character = input("Enter a 5-character word: ")
if len(five_character) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + single_character + " in " + five_character)

matches = 0

if single_character == five_character[0]:
    print(single_character + "found at index 0")
    matches = matches + 1
if single_character == five_character[1]:
    print(single_character + "found at index 1")
    matches = matches + 1
if single_character == five_character[2]:
    print(single_character + "found at index 2")
    matches = matches + 1
if single_character == five_character[3]:
    print(single_character + "found at index 3")
    matches = matches + 1
if single_character == five_character[4]:
    print(single_character + "found at index 4")
    matches = matches + 1

if matches != 0 and matches > 1:
    print(str(matches) + " instances of " + single_character + " found in " + five_character)
elif matches == 1:
    print(str(matches) + " instance of " + single_character + " found in " + five_character)
else:
    print("No instances of " + single_character + " found in " + five_character)

exit()