# Description:
# Create a simple game where a hero fights a monster.
# The game continues until either the hero or the monster's health reaches zero.
# Both the hero and the monster take turns attacking each other, and the damage dealt is randomized.
# The goal is to simulate a battle where the player can see how much health the hero and monster have left after each attack.



import random


def roll():
    min_value = 0
    max_value = 10
    roll = random.randint(min_value, max_value)

    return roll

while True:
    life = input('enter the max life capasity (50 -100): ')
    if life.isdigit():
        life = int(life)
        if 50 <= life <= 100:
            break
        else:
            print('must be between 50 - 100')
    else:
        print('invalid, try again')
print('we are starting get ready')

# hero = life
# monster = life

# def hero():
#     print('it\'s hero\'s turn and hero\' life is ', hero)
    





