# Choose Your Own Adventure
def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You are standing at a fork in the road. Do you want to go left or right?")
    choice1 = input("Type 'left' or 'right': ").lower()

    if choice1 == "left":
        print("You walk into a dark forest. You see a shiny object on the ground.")
        choice2 = input("Do you pick it up? Type 'yes' or 'no': ").lower()
        if choice2 == "yes":
            print("The object is a magical gem! It grants you powers. You win!")
        elif choice2 == "no":
            print("You walk away and miss out on a treasure. Game over.")
        else:
            print("Invalid choice. Game over.")
    elif choice1 == "right":
        print("You find yourself at the edge of a river. There's a boat nearby.")
        choice2 = input("Do you take the boat across? Type 'yes' or 'no': ").lower()
        if choice2 == "yes":
            print("You cross the river and find a hidden village. You win!")
        elif choice2 == "no":
            print("You decide not to cross and get lost in the woods. Game over.")
        else:
            print("Invalid choice. Game over.")
    else:
        print("Invalid choice. Game over.")

# Start the game
adventure_game()
