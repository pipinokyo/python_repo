import random

def roll(min_value=0, max_value=10):
    return random.randint(min_value, max_value)

def get_life_capacity():
    while True:
        life = input('Enter the max life capacity (50 - 100): ')
        if life.isdigit():
            life = int(life)
            if 50 <= life <= 100:
                return life
            else:
                print('Must be between 50 - 100')
        else:
            print('Invalid input, try again')

def hero_turn():
    while True:
        action = input("Choose action: [A]ttack, [H]eal: ").lower()
        if action in ['a', 'h']:
            return action
        else:
            print("Invalid action, choose again.")

def main():
    print('We are starting, get ready')
    life = get_life_capacity()
    hero_life = life
    monster_life = life
    potions = 3

    while hero_life > 0 and monster_life > 0:
        action = hero_turn()
        if action == 'a':
            hero_attack = roll()
            monster_life -= hero_attack
            print(f"Hero attacks Monster for {hero_attack} damage. Monster's life: {monster_life}")
        elif action == 'h' and potions > 0:
            heal_amount = roll(5, 15)
            hero_life += heal_amount
            potions -= 1
            print(f"Hero heals for {heal_amount}. Hero's life: {hero_life}. Potions left: {potions}")
        else:
            print("No potions left!")

        if monster_life > 0:
            monster_attack = roll()
            hero_life -= monster_attack
            print(f"Monster attacks Hero for {monster_attack} damage. Hero's life: {hero_life}")

        if hero_life <= 0:
            print("Hero has been defeated! Monster wins!")
        elif monster_life <= 0:
            print("Monster has been defeated! Hero wins!")

    if input("Game over. Do you want to play again? (y/n): ").lower() == 'y':
        main()

if __name__ == "__main__":
    main()