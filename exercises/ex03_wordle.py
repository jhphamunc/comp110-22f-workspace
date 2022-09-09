"""EX03 Real Wordle!"""

__author__ = "730560264"

from string import whitespace


contained_in_word: str = ""
secret_word: str = "codes"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, letter: str) -> str:
    assert len(letter) == 1
    i = 0
    contained_in_word = False
    while i < len(word):
        if word[i] == letter:
            contained_in_word = True
            i += 1
        else:
            i += 1
    return contained_in_word

def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    i = 0
    color_display: str = ""
    while i < len(secret):
        if contains_char(secret, guess[i]) == True and guess[i] == secret[i]:
            color_display = color_display + GREEN_BOX
        elif contains_char(secret, guess[i]) == True and guess[i] != secret[i]:
            color_display = color_display + YELLOW_BOX
        elif contains_char(secret, guess[i]) == False:
            color_display = color_display + WHITE_BOX
        i += 1
    print(color_display)

def input_guess(expected_length: str, turn_count: int) -> str:
    max_turn: int = 6  
    user_guess = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != int(expected_length):
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    if user_guess == secret_word:
        emojified(user_guess, secret_word)
        print(f"You won in {turn_count}/{max_turn} turns!") 
        exit()
        # try to figure out what is wrong with this/ find a better way to do this
    else:
        emojified(user_guess, secret_word)
    return user_guess

def main() -> None:
    current_turn: int = 1
    max_turn: int = 6 
    while current_turn <= max_turn:
        print(f"=== Turn {current_turn}/{max_turn} ===")
        input_guess(len(secret_word), current_turn)
        current_turn += 1
    else:
        print(f"X/{max_turn} - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()