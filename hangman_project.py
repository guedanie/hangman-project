# Objective of the project is to create a hangman game where the
# computer uses a randomly generated word, and ask the users to input 
# letter so see if they can guess the word. 
# test_word = "house"
# test_word = "mississippi"
import pandas as pd
# df = pd.read_csv('https://query.data.world/s/u2erxpyvtsazfatyrigoguunyoeg4p', encoding="iso-8859-1")


def pull_dictionary():
    words = pd.read_csv("word-meaning-examples.csv")
    return words

def return_index(words):
    random_sample = words.sample()
    random_index = random_sample.index
    return random_index

def return_word(index):
    random_sample = words.loc[index]
    random_sample = random_sample.values[0]
    test_word = random_sample[0].lower()
    return test_word
    
def return_meaning(index):
    random_sample = words.loc[index]
    random_sample = random_sample.values[0]
    meaning = random_sample[1].lower()
    return meaning


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
    
# def correct_letter_checker():
#     new_dashes = ''
#     win_score = 0
#     lose_score = 0
#     dashes = list(return_dashes(n_letters(test_word)))
#     while True:
#         print("What letter do you want to check")
#         user_input = input("")
#         correct_letter_index = test_word.find(user_input)
#         if correct_letter_index != -1:
#             dashes[correct_letter_index] = user_input
#             print(dashes)
#             win_score += 1
#             if win_score >= n_letters(test_word):
#                 new_dashes = new_dashes.join(dashes)
#                 print(f"You did it! The correct word was {new_dashes}")
#                 break
#         else: 
#             print("Wrong Choice")
#             lose_score += 1
#             if lose_score >= 6:
#                 print("You hang")
#                 break


def correct_letter_checker():
    new_dashes = ''
    win_score = 0
    lose_score = 0
    dashes = list(return_dashes(n_letters(test_word)))
    while True:
        print("What letter do you want to check")
        user_input = input("")
        correct_letter_index = [i for i in range(len(test_word)) if test_word.startswith(user_input, i)]
        print(correct_letter_index )
        if len(correct_letter_index) > 0:
            for x in correct_letter_index:
                dashes[x] = user_input
            print(dashes)
            win_score += 1
            if win_score >= len(set(test_word)):
                new_dashes = new_dashes.join(dashes)
                print(f"You did it! The correct word was {new_dashes}")
                break
        else: 
            print("Wrong Choice")
            lose_score += 1
            if lose_score == 1:
                clue_1(test_word)
            if lose_score == 5:
                print("You have one more try, the meaning of the word is: ")
                print(return_meaning(return_index))
            elif lose_score >= 6:
                print(f"You hang, the correct word was {test_word}")
                break

# Clues

# Clue 1 - how many vowels
def clue_1(test_word):
    vowel_counter = 0
    vowels = ('aeoiu')
    for x in test_word:
        if x in vowels:
            vowel_counter += 1
    print(f"The word has {vowel_counter} vowels")


# Clue 2 - first letter

def clue_first(test_word):
    clue_2 = test_word[0]
    print(f"The first letter of the word is {clue_2}")

def clue_last(test_word):
    clue_3 = test_word[-1]
    print(f"The first letter of the word is {clue_3}")

# Clue 3 - last letter
# Clue 4 - meaning



# Need to create a second loop to let players play again

# Need a function to display words that have already been guessed 

# need to create need functions to limit the input to only strings that aren't digits and no more than one character at a time

# need to write function to pull randomly generated word - ideally find a list of dictionaries in a JSON
# file with word definitions to give clues or be education. 

# work on developing a GUI 





# ------------------------------- #
#              Game Loop          #
# ------------------------------- #

words = pull_dictionary()
while True:
    test_word = return_word(return_index)
    print(test_word)
    intro()
    print("")
    print_dashes(n_letters(test_word))
    print("")
    print_n_letters(n_letters(test_word))
    print("")
    correct_letter_checker()
    break



# df = df[["first", "last", 'Species Common Name', 'Scientific Name', 'TaxonClass',
#        'Overall Sample Size ', 'Overall MLE', 'Overall CI - lower',
#        'Overall CI - upper', 'Male Sample Size', 'Male MLE', 'Male CI - lower',
#        'Male CI - upper', 'Female Sample Size ', 'Female MLE',
#        'Female CI - lower', 'Female CI - upper', 'Male Data Deficient',
#        'Female Data Deficient']]

# df["first"] + " " + df["last"]  

# df["first"].astype(str).str.cat(df["last"].astype(str), sep = ' ') 