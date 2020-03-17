# Objective of the project is to create a hangman game where the
# computer uses a randomly generated word, and ask the users to input 
# letter so see if they can guess the word. 
test_word = "house"


def intro():
    print("")
    print("Howdy there, wanna play a game of hangman?")
    print("")
    print("You have 6 tries to guess the word, or you hang")

def n_letters(test_word):
    length = len(test_word)
    return length

def print_dashes(length):
    dashes = " _"
    dashes *= length
    print(dashes)
    print("")

def return_dashes(length):
    dashes = "_"
    dashes *= length
    return dashes
    

def print_n_letters(length):
    print(f"We are looking for a word with {length} letters")

def get_user_input():
    print("What letter do you wnat to check")
    user_input = input("")
    return user_input

def check_if_letter_in_word(user_input):
            correct_letter_index = test_word.find(user_input)
            return correct_letter_index


def print_new_dashes(correct_letter_index, correct_letter, length):
    dashes = "_"
    dashes *= length
    dashes = list(dashes)
    dashes[correct_letter_index] = correct_letter
    new_dashes = ''
    new_dashes = new_dashes.join(dashes)
    print(new_dashes)


def letter_checker(correct_letter_index, user_input):
    check_if_letter_in_word(get_user_input())
    if correct_letter_index != -1:
        print_new_dashes(correct_letter_index, user_input, n_letters(test_word))
    else: 
        print("That is wrong")
        print_dashes(n_letters(test_word))
    
def correct_letter_checker():
    new_dashes = ''
    win_score = 0
    lose_score = 0
    dashes = list(return_dashes(n_letters(test_word)))
    while lose_score <= 6 or win_score <= 5:
        print("What letter do you want to check")
        user_input = input("")
        correct_letter_index = test_word.find(user_input)
        if correct_letter_index != -1:
            dashes[correct_letter_index] = user_input
            new_dashes = new_dashes.join(dashes)
            print(new_dashes)
            win_score += 1
        else: 
            print("Wrong Choice")
            lose_score += 1
    print("You hang")










# ------------------------------- #
#              Game Loop          #
# ------------------------------- #


while True:
    intro()
    print("")
    print_dashes(n_letters(test_word))
    print("")
    print_n_letters(n_letters(test_word))
    print("")
    correct_letter_checker()
    break
