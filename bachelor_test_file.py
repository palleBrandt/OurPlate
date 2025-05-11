import random

def create_new_player(name):
    return {
        'name': name,
        'hp': 100,
        'attack': (10, 20),
        'potions': 4
    }

def do_attack(attacker, defender):
    damage = random.randint(*attacker['attack'])
    defender['hp'] -= damage
    print(f"{attacker['name']} super attacks {defender['name']} for {damage} damage!")

def use_potions(player):
    if player['potions'] > 0:
        heal = random.randint(15, 300)
        player['hp'] += heal
        player['potions'] -= 1
        print(f"{player['name']} uses a potion and heals {heal} HP!")
    else:
        print(f"{player['name']} unfortunately has no potions left!")

def is__still_alive(player):
    return player['hp'] > 0

def take_player_turn(player, enemy):
    print(f"\n{player['name']}'s turn:")
    choice = input("Choose action (attack/potion): ").strip().lower()
    if choice == 'attack':
        attack(player, enemy)
    elif choice == 'potion':
        use_potion(player)
    else:
        print("Invalid choice. Turn skipped!")

def take_enemy_turn(enemy, player):
    print(f"\n{enemy['name']}'s turn:")
    if enemy['hp'] < 50 and enemy['potions'] > 0:
        use_potion(enemy)
    else:
        attack(enemy, player)

def fight(player, enemy):
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
    player_name = input("Enter your character's fighter name: ")
    player = create_player(player_name)
    enemy = create_player("Goblin Kings Father")
    battle(player, enemy)

if __name__ == "__main__":
    main()
