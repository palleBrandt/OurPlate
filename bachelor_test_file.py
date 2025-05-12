import random

def create_player(name):
    return {
        'name': name,
        'hp': 100,
        'attack': (10, 20),
        'potions': 4
    }

def attack(attacker, defender):
    """
Attacks the defender with a random amount of damage.

Args:
    attacker (dict): A dictionary containing information about the attacking character.
        - 'attack' (tuple): The range of possible attack values.
        - 'name' (str): The name of the attacking character.
    defender (dict): A dictionary containing information about the defending character.
        - 'hp' (int): The current hit points of the defending character.

Returns:
    None

Raises:
    ValueError: If the attacker or defender dictionaries do not contain the required keys.
"""
damage = random.randint(*attacker['attack'])
    defender['hp'] -= damage
    print(f"{attacker['name']} super attacks {defender['name']} for {damage} damage!")

def use_potion(player):
    """
Use a Potion on a Player

This function allows the player to use a potion, healing their health points.

Parameters
----------
player (dict): A dictionary containing information about the player.
             It should have the following keys:
             - 'potions' (int): The number of potions available.
             - 'name' (str): The name of the player.
             - 'hp' (int): The current health points of the player.

Returns
-------
None

Raises
------
None

Example
-------
use_potion(player={'name': 'John', 'potions': 2, 'hp': 100})
"""
if player['potions'] > 0:
        heal = random.randint(15, 300)
        player['hp'] += heal
        player['potions'] -= 1
        print(f"{player['name']} uses a potion and heals {heal} HP!")
    else:
        print(f"{player['name']} unfortunately has no potions left!")

def is_alive(player):
    """
Checks if a player is alive based on their hit points.

Args:
    player (dict): A dictionary containing the player's attributes, including 'hp'.

Returns:
    bool: True if the player has more than zero hit points, False otherwise.
"""
return player['hp'] > 0

def player_turn(player, enemy):
    print(f"\n{player['name']}'s turn:")
    choice = input("Choose action (attack/potion): ").strip().lower()
    if choice == 'attack':
        attack(player, enemy)
    elif choice == 'potion':
        use_potion(player)
    else:
        print("Invalid choice. Turn skipped!")

def enemy_turn(enemy, player):
    print(f"\n{enemy['name']}'s turn:")
    if enemy['hp'] < 50 and enemy['potions'] > 0:
        use_potion(enemy)
    else:
        attack(enemy, player)

def battle(player, enemy):
    print("Battle Start!")
    while is_alive(player) and is_alive(enemy):
        player_turn(player, enemy)
        if not is_alive(enemy):
            print(f"{enemy['name']} is defeated! You win!")
            break
        enemy_turn(enemy, player)
        if not is_alive(player):
            print(f"{player['name']} is defeated! Game over.")
            break
        print(f"\n{player['name']} HP: {player['hp']} | {enemy['name']} HP: {enemy['hp']}")

def main():
    player_name = input("Enter your character's name: ")
    player = create_player(player_name)
    enemy = create_player("Goblin Kings Father")
    battle(player, enemy)

if __name__ == "__main__":
    main()