import time
import random

def print_pause(print_message):
    print(print_message)
    time.sleep(2)

tools = ["consistency", "time management", "a mentor", "patience", "confidence"]
random_tool = random.choice(tools)

def intro():
    print_pause("You find yourself in a season of transition. ")
    print_pause("You are faced with a decision to stay in your current, unfulfilling career...")
    print_pause("Or to take the journey into Software Engineering.")

def tech_journey(user_tools):
    print_pause("Enter 1 to stay at your current job.")
    print_pause("Enter 2 to take the journey into Software Engineering.")
    print_pause("What would you like to do?")

    user_choice = input("Please enter 1 or 2. > ")
    if user_choice == '1':
        print_pause("That's okay. Maybe now isn't the right time for you.")
    elif user_choice == '2':
        print_pause("Congrats! You have made the brave decision to journey into tech.")
        user_tools.append("courage")
        print_pause(f"To assist you on your journey you are gifted with {random_tool}!")
        user_tools.append(random_tool)
        learning_path(user_tools)

def learning_path(user_tools):
    print_pause("Now that you've decided to journey into tech. It's time to choose a learning path.")
    print_pause("Enter 1 to go the self-taught path.")
    print_pause("Enter 2 to enroll in a structured Bootcamp.")
    print_pause("What would you like to do?")

    user_choice = input("Please enter 1 or 2. > ")
    if user_choice == '1':
        self_taught(user_tools)
        power_up(user_tools)
    elif user_choice == '2':
        bootcamp(user_tools)
        power_up(user_tools)
       
def power_up(user_tools):
    print_pause("Please choose a tool to assist you on this journey: ")
    tools = input("consistency - time management - a mentor - resourcefulness - confidence\n")
    user_tools.append(tools)

def self_taught(user_tools):
    list = ' '.join(user_tools)
    print_pause(f"You are currently equipped with {list}.")
    print_pause("It's a month into self-study and have a lot of competing priorities. ")
    if "time management" in user_tools:
        print_pause("Luckily you have your time management tool to assist you. "
        "And you continue to progress.")
        job_search(user_tools)
    elif "consistency" in user_tools:
        print_pause("Luckily you have your consistency tool to assist you. "
        "And you continue to progress.")
        job_search(user_tools)
    else:
        print_pause("You might need another tool to assist you.")
        power_up(user_tools)
    job_search(user_tools)
    end_game(user_tools)

def bootcamp(user_tools):
    list = ' '.join(user_tools)
    print_pause(f"You are currently equipped with {list}.")
    print_pause("It's a month into your Bootcamp and are struggling to work through the more complex bugs in your programs. ")
    if "resourceful" in user_tools:
        print_pause("Luckily you have your resourceful tool to assist you. "
        "And you continue to progress.")
        job_search(user_tools)
    elif "consistency" in user_tools:
        print_pause("Luckily you have your consistency tool to assist you. "
        "And you continue to progress.")
        job_search(user_tools)
    else:
        print_pause("You might need another tool to assist you.")
        power_up(user_tools)
    job_search(user_tools)
    end_game(user_tools)

def job_search(user_tools):
    print_pause("You are now ready to begin the job search.")
    list = ' '.join(user_tools)
    print_pause(f"You are currently equipped with {list}.")
    print_pause("After a month of submitting applicatiosn you are experiencing imposter syndrome. ")
    print_pause("You can fight this with one of your tools!")
    weapon = input(f"Which tool would you like to use: {list} >> ")
    if weapon in list:
        print_pause("Congratulations! You have defeated imposter syndrome.")
        end_game(user_tools)
    else:
        print_pause("You do not have the correct tool.")

def end_game(user_tools):
    if len(user_tools) >= 2:
        list = ' '.join(user_tools)
        print_pause(f"Equipped with {list}. You now have everything you need to land that first Software Engineering role!")
    else:
        restart()

def restart():
    play_again = input("Would you like to play the game again? Y or N > ").lower()
    if play_again == 'y':
        play_game()
    elif play_again == 'n':
        print_pause("Thank you for playing. Goodbye!")
    else:
        print_pause("Please enter either 'y' or 'n' > ")
    
    
def play_game():
    user_tools = []
    intro()
    tech_journey(user_tools)

play_game()

# Game should end when user_tools >= 2