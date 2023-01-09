import time
import random

obstacles = ["angry crocodile", "monsoon", "hoard of monkeys"]
tools = ["small hatchet", "magical sword"]

def print_pause(print_message):
    print(print_message)
    time.sleep(2)

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt)
        if option1 == response:
            break
        elif option2 == response:
            break
    return response

def intro():
    print_pause("You find yourself standing in the middle of a tropical beach. ")
    print_pause("Rumor has it there is a hidden treasure somewhere on the island...")

def treasure_hunt(tool, obstacle):
    print_pause("Enter 1 to journey up the mountain.")
    print_pause("Enter 2 to continue along the beach.")
    user_choice = valid_input("What would you like to do?\n > Please enter 1 or 2. ", "1", "2")
    if user_choice == '1':
        mountain(tool, obstacle)
    elif user_choice == '2':
        beach(tool, obstacle)
    
def mountain(tool, obstacle):
    if (tool == tools[0]):
        print_pause("You begin to journey up the mountain. Using your small hatchet to clear your path.")
        print_pause("You suddenly spot a shimmer of gold.")
        print_pause("It is not the buried treasure...\nbut a magical sword!")
        print_pause("You head back to the beach with your new sword.")
        
    else:
        print_pause("You've already been down this path and have retrieved all of the necessary tools.")
        print_pause("You head back to the beach.")
    treasure_hunt(tool, obstacle)

def beach(tool, obstacle):
    print_pause("You begin walking down the beach.")
    print_pause("You come to a river and see a small boat on the shore.")
    print_pause("You get in the boat and begin floating down the river.")
    print_pause(f"All of a sudden a {obstacle} comes out of nowhere!")
    if tool == tools[1]:
        print_pause(f"You use the magical powers of your sword to defeat the {obstacle}.")
        print_pause("You continue to float along the river that leads you to a cave.")
        print_pause("You slowly approach the cave using your magical sword as a light.\nAnd find the hidden treasure sparkling with gold and jewels!")
        restart()
    else:
        print_pause(f"Your small hatchet has left you helpless and you paddle quickly back to the beach!")
    treasure_hunt(tool, obstacle)

def restart():
    user_choice = valid_input("Would you like to play the game again? Y or N > ", 'y', 'n').lower()
    if user_choice == 'y':
        print_pause("Awesome! Restarting...")
        play_game()
    elif user_choice == 'n':
        print_pause("Thank you for playing. Goodbye!")
    
def play_game():
    tool = tools[0]
    obstacle = random.choice(obstacles)
    intro()
    treasure_hunt(tool, obstacle)

play_game()
