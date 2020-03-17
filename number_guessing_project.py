import random
x = 1
y = 20

#####################
#### FUNCTIONS ######
#####################

def game_intro():
    print("Wanna play a game?")
    print()
    print(f"I am thinking of a number between {x} and {y}")

def game_intro_two():
    print("Here we go again!")
    print()
    print(f"I am thinking of a number between {x} and {y}")

def user_choice():
    while True:
        print("Can you guess the number that I am thinking of?")
        user_input = input("")
        if user_input.isdigit():
            return int(user_input)
            break
        else:
            print(f"You need to type a number, {user_input} is not a valid number")
    
def clue_even_or_odd():
    clue_1 = random_int % 2
    if clue_1 == 0:
        print("The number that I am thinking of is even")
    else:
        print("The number that I am thinking of is odd")

def clue_greater_less_than():
    clue_2 = user_input - random_int
    if clue_2 < 0:
        print(f"The number i am thinking of is larger than {user_input}")
    else:
        print(f"The number i am thinking of is smaller than {user_input}")

def turn_counter(number_turns):
    main = "That's not the number I am thinking of!"
    first = "That was your first try"
    second = "That was your second try"
    third = "That was your last try! You will have to try again"
    if number_turns == 1:
        print()
        print(f"{main} {first}")
        print()
        clue_greater_less_than()
        print()
    elif number_turns == 2:
        print()
        print(f"{main} {second}")
        print()
        clue_even_or_odd()
        print()
    else:
        print()
        print(f"{main} {third}")

def play_again():
    user_selection = input("Would you like to play again? ")
    user_selection = user_selection.lower()
    if user_selection[0] == "y":
        user_selection = "y"
        print()
        game_intro_two()
        return user_selection
    else:
        user_selection = "n"
        print("Too bad!")
        return user_selection

def tell_asnwer():
    print()


        
########################
###### GAME LOOP #######
########################

print()
game_intro()
while True:
    random_int = random.randint(x,y)
    user_input = 0
    # print(random_int)
    number_turns = 0
    
    while True:
        user_input = user_choice()
        if user_input != random_int:
            number_turns += 1
            turn_counter(number_turns)
            if number_turns == 3:
                print("")
                print(f"The number I was thinking of was {random_int}")
                print("")
                break               
        else:
            print(f"You did it! {random_int} was the number I was thinking!")
            break
    
    user_selection = input("Would you like to play again? (y/n) ")
    user_selection = user_selection.lower()
    if user_selection[0] == "y":
        user_selection = "y"
        print()
        game_intro_two()
    else:
        print("Too bad!")
        break
    


