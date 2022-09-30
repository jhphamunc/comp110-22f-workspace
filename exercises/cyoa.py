"""This is ex06 Choose Your Own Activity!"""

__author__ = "730560264"


from random import randint


points: int = 0
player: str = ""
max_attack: int = 10

SWORD: str = ("\U0001F5E1")
SHIELD: str = ("\U0001F6E1")
STAR: str = ("\U00002B50")

day_counter: int = 0


def greet() -> None:
    """Greet function welcomes the player to the game."""
    print("Welcome to the Battle RNG, a game where you can\nchoose to battle or scavenge the choice is yours.")
    global player
    player = input("First, what do you want to be called? ")
    print(f"Welcome {player}, while in game choose the option to battle(1), scavenge(2) or end the game(3).")
    print("Battling will allow you to attack(1) or defend(2) from an attack\nchoosing to attack will allow you to gain or lose points and")
    print("choosing to defend will save your points but your attack damage may fall.\nWhile scavenging will allow you to possibly get stronger.")


def main() -> int:
    """Main function begins the procedure."""
    greet()
    player_choice: int = 0
    game_continue: bool = True
    global day_counter
    global max_attack
    while game_continue is True and max_attack > 0:
        print(f"Current points: {points} {STAR}")
        print(f"Current attack damage: {max_attack} {SWORD}")
        print(f"======= Day {day_counter} =======")
        player_choice = int(input("Write the number you\'d like to do; battle(1), scavenge(2) or end the game(3): "))
        while player_choice > 3 or player_choice < 0:
            player_choice = int(input("Please write one of the numbers; battle(1), scavenge(2) or end the game(3): "))
        if player_choice == 1:
            battle()
        elif player_choice == 2:
            scavenge()        
        elif player_choice == 3:
            game_continue = False
        day_counter += 1
    if game_continue is False:
        print(f"Final points: {points} {STAR}")
        print(f"Thank you, {player} for participating in the game. Hope you enjoyed!")
    elif max_attack <= 0:
        print(f"{player} couldn\'t survive the night after the enemies\'s invasion")
        print(f"Current points: {points} {STAR}")
    return points


def battle() -> None:
    """Option 1 for one of the first 3 options to choose from."""
    player_battle_choice: int = 0
    player_battle_choice = int(input("Write the number you\'d like to do; attack(1) or defend(2): "))
    while player_battle_choice < 1 or player_battle_choice > 2:
        player_battle_choice = int(input("Please write the number you\'d like to do; attack(1) or defend(2): "))
    if player_battle_choice == 1:
        return attack()
    elif player_battle_choice == 2:
        return defend(max_attack)


def attack() -> int:
    """From battle option, allows the player to attack."""
    attack_damage: int = randint(1, max_attack)
    enemy_defense: int = randint(1, max_attack - 2) 
    global points
    global player
    if attack_damage > enemy_defense:
        points_up: int = attack_damage - enemy_defense
        points += points_up
        print(f"After a long and hard battle {player} won the fight, inflicting {points_up} damage to the enemy {SWORD}!")
        return points
    elif attack_damage < enemy_defense:
        points_down: int = enemy_defense - attack_damage
        points -= points_down
        print(f"After a long and hard battle {player} lost the battle, losing {points_down} points {SWORD}!")
        return points
    elif attack_damage == enemy_defense:
        print(f"After a long and hard battle {player} took no damage {SWORD}!")
        return points


def defend(defense_power: int) -> int:
    """From battle option, allows the player to defend."""
    global player
    global max_attack
    max_lost: int = round(defense_power / 3)
    subtract_attack: int = randint(0, max_lost)
    max_attack -= subtract_attack
    if defense_power > 0:
        print(f"After a successful night of defending, {player} lost {subtract_attack} attack damage {SHIELD}!")
    else:
        print(f"{player} lost {subtract_attack} and passed out")
    return max_attack


def scavenge() -> None:
    """Allows the player to look for more attack damage."""
    global max_attack
    global player
    random_selection: int = randint(1, 10)
    if random_selection < 7:
        random_attack_increase: int = randint(1, 7)
        max_attack += random_attack_increase
        print(f"While scavenging {player} gained {random_attack_increase} attack damage!")
    else:
        random_attack_decrease: int = randint(1, 4)
        max_attack -= random_attack_decrease
        print(f"While scavenging {player} was attacked and lost {random_attack_decrease} attack damage!")


if __name__ == "__main__":
    main()
    """Begins the function."""