# DICE ROLLING SIMULATOR

import random

DiceRolling = True

while DiceRolling:
    print(random.randint(1,6))
    PlayAgain = input("Do You Want to Roll Again? [y/n]:")
    if PlayAgain == "y":
        continue
    else:
        print("Game Over!")
        break











