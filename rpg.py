import random

player_name = input("Enter your hero's name: ")

health = 100
gold = 0
potions = 2

print(f"\nWelcome, {player_name}! You have entered the Shadow Forest.")

while health > 0:
    print("\n--- MENU ---")
    print("1. Explore the forest")
    print("2. View inventory")
    print("3. Drink a potion")
    print("4. Exit game")

    choice = input("Choose an option: ")

    if choice == "1":
        event = random.choice(["gold", "enemy", "nothing"])

        if event == "gold":
            found_gold = random.randint(5, 20)
            gold += found_gold
            print(f"You found {found_gold} gold coins!")

        elif event == "enemy":
            enemy_health = 40
            print("\nA wild goblin appears!")

            while enemy_health > 0 and health > 0:
                print(f"\nYour Health: {health}")
                print(f"Goblin Health: {enemy_health}")
                print("1. Attack")
                print("2. Run Away")

                battle_choice = input("Choose an action: ")

                if battle_choice == "1":
                    damage = random.randint(10, 25)
                    enemy_health -= damage
                    print(f"You dealt {damage} damage!")

                    if enemy_health > 0:
                        enemy_damage = random.randint(5, 18)
                        health -= enemy_damage
                        print(f"The goblin dealt {enemy_damage} damage!")

                elif battle_choice == "2":
                    print("You escaped from the battle!")
                    break

                else:
                    print("Invalid choice.")

            if enemy_health <= 0:
                reward = random.randint(10, 30)
                gold += reward
                print(f"You defeated the goblin and earned {reward} gold!")

        else:
            print("You explored the area but found nothing.")

    elif choice == "2":
        print("\n--- INVENTORY ---")
        print(f"Health: {health}")
        print(f"Gold: {gold}")
        print(f"Potions: {potions}")

    elif choice == "3":
        if potions > 0:
            health += 30
            if health > 100:
                health = 100

            potions -= 1
            print("You drank a potion and restored health.")

        else:
            print("You don't have any potions left.")

    elif choice == "4":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice.")

if health <= 0:
    print("\nYou have died. Game Over.")