##TEXT-BASED ADVENTURE GAME
answer = input("Do you want to play this game? [Yes/no]:")
if answer == "yes":
    print("Welcome to the game!")
    answer = input("Do you want to play Football or Cricket? [Football/Cricket]:")
    if answer == "Football":
        print("You will meet with Leonel Messi.")
    elif answer == "Cricket":
        print("You will meet with Virat Kohli.")
        answer = input("Do you want to play with them or run away! [play/no]")
        if answer == "play":
            print("You are very lucky! You meet with them.")
        else:
            print("You are Unlucky! You don't meet with them.")

else:
    print("The game is over!")






