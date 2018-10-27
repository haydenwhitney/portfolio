#hayden Whitney
#10/18
#Combat System

import random

print("An unruly monster approaches...")

win = 0
mHealth = 100
pHealth = 100
choice = input("Would you like to flee the battle or stay and attack? ")

while choice == "attack":
    pDamage = random.randrange(0, 25)
    mDamage = random.randrange(0, 50)
    if pDamage == 0:
        print("You missed.")
    else:
        print("You attack the monster with a power of", pDamage)
    mHealth -= pDamage
    if mHealth > 0:
        pHealth -= mDamage
        print("The monster attacks you with a power of", mDamage)
    if pHealth <= 0:
        win = 0
        print("You died.")
        break
    elif mHealth <= 0:
        win = 1
        print("You defeated the monster.")
        break
    elif mHealth >= 0 and pHealth >= 0:
        print("You have ", pHealth, "health.")
        print("The monster has ", mHealth, "health.")
        choice = input("Would like to flee the battle or stay and attack? ")
        if choice != "attack" and choice != "flee":
            print("I'm not sure what that is.")
            continue
    else:
        continue

if choice == "flee":
    print("You're a coward.")
if win == 0:
    print("Game Over.")
else:
    print("You win.")


