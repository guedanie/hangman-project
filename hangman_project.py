# Objective of the project is to create a hangman game where the
# computer uses a randomly generated word, and ask the users to input 
# letter so see if they can guess the word. 
# test_word = "house"
# test_word = "mississippi"
import pandas as pd

# If the csv file doesn't exist in the directory - this will pull it from data.world
# def pull_list_of_words():
    # words = pd.read_csv('https://query.data.world/s/mfp7lfkxfott7zp2sgr3nlfv4v5bpp', encoding= "iso-8859-1")
    # words.to_csv("word-meaning-examples.csv")

# ------------------------------- #
#           Functions             #
# ------------------------------- #

# Function to allow users to select what level they want to play at. 
# Basically, the easier levels use shorter words, while harder levels pick longer words
def level_picking(words):
    active = True
    while active:
        print("What level do you want to choose")
        print("1 = Easy, 2 = Medium, 3 = Hard")
        user_level_selection = input("")
        easy_filter = words[words["Word"].str.len().isin(range(1,5))]
        medium_filter = words[words["Word"].str.len().isin(range(6,9))]
        hard_filter = words[words["Word"].str.len() > 8]
        if user_level_selection == "1":
            filter_words = easy_filter
            return filter_words
            active = False
            
        elif user_level_selection == "2":
            filter_words = medium_filter
            return filter_words
            active = False
            
        elif user_level_selection == "3":
            filter_words = hard_filter
            return filter_words
            active = False
            
        else:
            print("Please enter a valid choice")
      
        
# Function to read the csv dictionary. It has to be in the same directory
def pull_dictionary():
    words = pd.read_csv("word-meaning-examples.csv")
    return words

# Function to randomly select an index, based on the filtered list of words supplied
# by the level pick function
def return_index(filter_words):
    random_sample = filter_words.sample()
    random_index = random_sample.index
    return random_index

## Once we have an index, we can find and get the value of the word from the original list
# of words
def return_word(index):
    random_sample = words.loc[index]
    random_sample = random_sample.values[0]
    test_word = random_sample[0].lower()
    return test_word

# Similar as the function above, this uses the index to pull the definition of the word
def return_meaning(index):
    random_sample = words.loc[index]
    random_sample = random_sample.values[0]
    meaning = random_sample[1].lower()
    return meaning

# Intro intro
def intro():
    print("")
    print("Howdy there, wanna play a game of hangman?")
    print("")
    print("You have 6 tries to guess the word, or you hang")

# Measure length of word
def n_letters(test_word):
    length = len(test_word)
    return length

# Prints the original blank dashes to visualize how many letters are in the word
def print_dashes(length):
    dashes = " _"
    dashes *= length
    print(dashes)
    print("")

# Stores the dashes for other functions to use 
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
    
# Main function - three loops to get user input, verify that the input is valid, and then check
# if the letter inputed is part of the word we are looking for. 
def is_letter_in_word():
    new_dashes = ''
    win_score = 0
    lose_score = 0
    correct_list = []
    dashes = list(return_dashes(n_letters(test_word))) # Turned the dashes into a list for easier manupulation
    inPlay = True
    while inPlay: # Main loop
        invalid = True
        while invalid: 
            print("Please enter a letter")
            user_input = input("").lower()
            duplicate = True
            while duplicate: # subloop dedicated to ensuring the input hasn't already been inputed before. 
                if user_input not in correct_list:
                    duplicate = False 
                else:
                    print("You already enter that letter, please enter a new one")
                    user_input = input("").lower()
            # Loop below dedicated to ensure input is valid       
            if check_if_digit(user_input) == False and check_length(user_input) == True and check_if_special_char(user_input) == False:
                invalid = False
            else: 
                print(f"Please enter a valid letter, {user_input} doesn't work")
        correct_list.append(user_input) # if input is valid, it then runs through the list comprehension to see if it matches any of the letter in the test_word
        correct_letter_index = [i for i in range(len(test_word)) if test_word.startswith(user_input, i)]
        if len(correct_letter_index) > 0: # if correct, it updates the by replacing the letter at the correct index, the list comprehension above pulls the index
            for x in correct_letter_index:
                dashes[x] = user_input
            print(dashes)
            print("")
            print(f"The letters already guessed are: {correct_list}")
            print("")
            print(f"You have {6 - lose_score} tries left before you hang")
            print("")
            win_score += 1 # Tracker of points, so that the game knows when to end
            if win_score >= len(set(test_word)):
                new_dashes = new_dashes.join(dashes)
                print(f"You did it! The correct word was {new_dashes}")
                inPlay = False # breaks the main loop
        else: 
            print("Wrong Choice") # if input is incorrect, it display wrong choice, and increases the counter for number of turns
            print("")
            print(dashes)
            print("")
            print(f"The letters already guessed are: {correct_list}")
            print("")
            lose_score += 1 
            print(f"You have {6 - lose_score} tries left before you hang")
            if lose_score == 1: # I have added two clues to help the user, the first will be given after the first wrong input, and it shows the number of vowels in the word
                print("")
                clue_1(test_word)
                print("")
            if lose_score == 5: # on their last turn, it shows players the word definition for further help
                print("You have one more try, the meaning of the word is: ")
                print("")
                print(return_meaning(index))
                print("")
            elif lose_score >= 6: # if counter is 6 - then the game is over
                print(f"You hang, the correct word was {test_word}")
                inPlay = False    


        

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
def pay_again():
    print("Would you like to play again? (y/n) ")
    user_selection = input("")
    return user_selection.lower()

# Need a function to display words that have already been guessed 

# need to create need functions to limit the input to only strings that aren't digits and no more than one character at a time

# Should come back false
def check_if_digit(user_input):
    return str(user_input).isdigit()

# SHould come back as false 
def check_length(user_input):
    return len(user_input) == 1

def check_if_special_char(user_input):
    special_chars = ("@!#$%^&*()[]|\><.,?/+=_")
    return user_input in special_chars

## Further ideas:

# drawing the stick man using variables, and then printing those variables as a visualization
# work on developing a GUI 





# ------------------------------- #
#              Game Loop          #
# ------------------------------- #

#pull_list_of_words() # Function used to pull the list of words from data.world - this will create a new file in the same directory as this program
words = pull_dictionary()
new_dashes = ''
win_score = 0
lose_score = 0
while True:
    intro()
    filter_words = level_picking(words)
    index = return_index(filter_words)
    test_word = return_word(index)
    test_meaning = return_meaning(index)
    # print(test_word)
    # print(test_meaning)
    print("")
    print_dashes(n_letters(test_word))
    print("")
    print_n_letters(n_letters(test_word))
    print("")
    # correct_letter_checker()
    is_letter_in_word()
    user_selection = pay_again()
    if user_selection == "y":
        continue
    else:
        print("Hope not to see you near the knot again")
        break



## This HTML link is to an animal names list - for use later
# df = pd.read_csv('https://query.data.world/s/u2erxpyvtsazfatyrigoguunyoeg4p', encoding="iso-8859-1")

# df = df[["first", "last", 'Species Common Name', 'Scientific Name', 'TaxonClass',
#        'Overall Sample Size ', 'Overall MLE', 'Overall CI - lower',
#        'Overall CI - upper', 'Male Sample Size', 'Male MLE', 'Male CI - lower',
#        'Male CI - upper', 'Female Sample Size ', 'Female MLE',
#        'Female CI - lower', 'Female CI - upper', 'Male Data Deficient',
#        'Female Data Deficient']]

# df["first"] + " " + df["last"]  

# df["first"].astype(str).str.cat(df["last"].astype(str), sep = ' ') 