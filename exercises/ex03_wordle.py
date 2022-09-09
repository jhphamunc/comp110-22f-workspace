"""EX03 Real Wordle!"""

__author__ = "730560264"

secret_word: str = "codes"
# sets up the secret word that can be easily changed

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# sets up the colored boxes to indicate correct/ wrong


def contains_char(word: str, letter: str) -> bool: 
    """defines the contains char function which goes through the secret word using one letter of the guess at a time"""
    assert len(letter) == 1
    i = 0
    contained_in_word = False
    # predetermines the value to be false unless otherwise
    while i < len(word):
        if word[i] == letter:
            contained_in_word = True
            # if the letter is found in the secret then the value becomes true
            i += 1
        else:
            i += 1
            # iterates through the whole guess
    return contained_in_word


def emojified(guess: str, secret: str) -> str: 
    """defines the emojified function which takes the contrains_char function and gives each index a colored box"""
    assert len(guess) == len(secret)
    i = 0
    color_display: str = ""
    while i < len(secret):
        if contains_char(secret, guess[i]) is True and guess[i] == secret[i]:
            color_display = color_display + GREEN_BOX
            # if the corresponding index is found in both secret and guess then a green box appears
        elif contains_char(secret, guess[i]) is True and guess[i] != secret[i]:
            color_display = color_display + YELLOW_BOX
            # if a letter of guess is found in secret but not at the same index a yellow box appears
        elif contains_char(secret, guess[i]) is False:
            color_display = color_display + WHITE_BOX
            # if the letter of guess is not found in secret then a white box appears
        i += 1
    print(color_display)
    # the display prints after the length of the secret word runs
    return color_display


def input_guess(expected_length: int) -> str: 
    """defines the input_guess function which makes sure the length of the guess is good"""
    user_guess = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != (expected_length):
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
        # if the length of guess is too long or too short an error appears and you get a chance to retry
    if len(user_guess) == len(secret_word):
        emojified(user_guess, secret_word)
        # as long as the length of guess is the same as the length of secret it goes to the emojified function
    return user_guess


def main() -> None: 
    """defines main function which is where the program begins"""
    current_turn: int = 1
    max_turn: int = 6 
    while current_turn <= max_turn:
        print(f"=== Turn {current_turn}/{max_turn} ===")
        # sets up the beginning code/ start of the program and the headings for each turn after
        if input_guess(len(secret_word)) == secret_word:
            print(f"You won in {current_turn}/{max_turn} turns!") 
            current_turn += max_turn + 1
            # if the guess is the secret word you win the game and no more guesses are given
        else:
            current_turn += 1
            # if you don't guess correct and you're under the max_turn you keep going
    if current_turn == 7:
        print(f"X/{max_turn} - Sorry, try again tomorrow!")
        # if you have exceeded the max_turn then the game is over


if __name__ == "__main__":
    main()