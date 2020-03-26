import pygame, sys
from pygame.locals import *
import time
import pandas as pd
import numpy as np
pygame.init()

###################################
###        Global Variables     ###
###################################


pygame.display.set_caption("Hangman")

win_height = 480  
win_width = 700

# Colors
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)

#Win and lose counters
win_counter = 0
lose_counter = 0

# Not a variable - but the main function that pulls a random index from the csv file. This in the variables section becasue the variables "test-word" and "index"
# need to be defined before they are called 

def select_secret_word():
    words = pd.read_csv("word-meaning-examples.csv")
    random_sample = words.sample()
    index = random_sample.index
    random_sample = words.loc[index]
    random_sample = random_sample.values[0]
    test_word = random_sample[0].lower()
    return test_word, index

# Varibles that hold the secret word, as well as the secret word's index which lets us pull the meaning
test_word_and_index = select_secret_word()
test_word = test_word_and_index[0].lower() 
index = test_word_and_index[1]

# Diplay_surface becomes the main window variables.
display_surface = pygame.display.set_mode((win_width, win_height))

# Stores all the images in a list. Because it is in a list, it makes it easier to actually move through all the images rathen than storing each in individual variables
hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'), pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'), pygame.image.load('hangman6.png')]

# buttons varible is used to draw the circles with the letters. The information for the circles is stored in this list 
buttons = []


letters = "abcdefghijklmnopqrstuvwxyz" 
labels = []
# stored all guessed letters
guessed = []
# Print the original "spaced-out word" becasue on the length of the secret word. 
dashes = "_" * len(test_word)


#################################
##         Main Functions      ##
#################################


#  This uses the index to pull the definition of the word
def return_meaning(index):
    words = pd.read_csv("word-meaning-examples.csv")
    random_sample = words.loc[index]
    random_sample = random_sample.values[0]
    meaning = random_sample[1].lower()
    return meaning



# General function used to display text, self-made "print" function
def message(text, posx, posy, fontsize):
    font = pygame.font.SysFont("freesansbold.ttf", fontsize)
    text = font.render(text, True, BLACK)
    textRect = text.get_rect()
    textRect.center = (posx, posy)
    display_surface.blit(text, textRect)

def button_label(text, posx, posy):
    font = pygame.font.SysFont("freesansbold.ttf", 30)
    text = font.render(text, True, WHITE)
    textRect = text.get_rect()
    textRect.center = (posx, posy)
    display_surface.blit(text, textRect)

def create_label_list():
    for i in letters:
        labels.append(i)

# Function used to draw the circles
def draw_circle(x, y):
    pygame.draw.circle(display_surface, BLUE, (x, y), 15, 0)

# Key function - used to populate the buttons list with the x,y position for each individual circle, as well as individual char_index used to match the word
def create_circles():
    increase = round(win_width / 13)
    for i in range(26):
        if i < 13:
            y = 40
            x = 25 + (increase * i)
            char_index = i
        else:
            x = 25 + (increase * (i - 13))
            y = 85
            char_index = i
        buttons.append([LIGHT_BLUE, x, y, 20, True, char_index])
        # buttons.append([color, x_pos, y_pos, radius, visible, char_index])

# Main function that redraws the window every turn, updating the circles, as well as the text
def draw_circles_and_labels():
    global lose_counter
    global dashes
    global guessed
    display_surface.fill(WHITE)

    display_surface.blit(hangmanPics[0 + lose_counter] , (win_width // 3, win_height // 3))

    message(str(dashes), 475, 350, 40)
    
    
    global buttons

    global labels 

    for i in range(len(buttons)):
        if buttons[i][4] == True:
            pygame.draw.circle(display_surface, BLUE, (buttons[i][1], buttons[i][2]),  15, 0)  
        
    for i in range(len(labels)):
        button_label(labels[i], buttons[i][1], buttons[i][2])

    message(f"Guessed letters: {str(guessed)}", 300, 400, 30)

    pygame.display.update()  

def buttonHit(x, y): # Function used to identify was button was selected by user. Uses window sizes to ensure a button was hit, and then narrows down the choice, returning the char_index for that button, which we can use to match to our label
    for i in range(len(buttons)):
        if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
            if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                return buttons[i][5]
    return None
        

def is_chr_in_word(letter): # Function used to update the list with the correctly guessed chars
    global dashes

    global letters

    correct_letter_index = [i for i in range(len(test_word)) if test_word.startswith(letters[letter], i)]

    dashes = list(dashes)
    for x in correct_letter_index:
        dashes[x] = letters[letter]
    dashes = ''.join(dashes)
    # dashes.replace(" ", "")
        
    
def end(winner=False): #Function used to end the game - and offer the opportunity to replay
    global index
    meaning = return_meaning(index)
    lostTxt = 'You Lost, press any key to play again...'
    winTxt = 'WINNER!, press any key to play again...'
    pygame.time.delay(1000)
    

    if winner == True:
        label = winTxt
        color = GREEN
    else:
        label = lostTxt
        color = RED

    display_surface.fill(color)

    message(label, win_width/2, win_height/2, 30)
    message(f"The word was: {test_word}", 475,350, 30)
    message(f"The meaning is: {meaning}", 375, 400, 30)

    pygame.display.update()

    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                again = False
    reset()
    
def reset(): # If player wants to play again, this resets all the global varibles and selects a new random word 
    global lose_counter
    global guessed
    global buttons
    global win_counter
    global dashes
    global letters
    global test_word
    global index
    for i in range(len(buttons)):
        buttons[i][4] = True
    test_word_and_index = select_secret_word()
    test_word = test_word_and_index[0]
    index = test_word_and_index[1]
    letters = "abcdefghijklmnopqrstuvwxyz" 
    guessed = []
    dashes = "_" * len(test_word)
    lose_counter = 0
    win_counter = 0
    
    

####################################
#           Game Loop              #
####################################

# print(test_word) # To be use for testing purposes only - will print the secret word onto the terminal

create_circles() 
    
create_label_list()

inPlay = True

while inPlay: # main game loop
    
    
    draw_circles_and_labels() # function that updates the game window
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            inPlay = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_position = pygame.mouse.get_pos()
            letter = buttonHit(click_position[0], click_position[1])
            if letter != None: # the following loops ensure that the guessed letter is in the secret word
                buttons[letter][4] = False # by turning this False, in ensure that the button is not drawn the next turn, removing them from the window
                guessed.append(letters[letter]) # add letter to the guessed letters
                if letters[letter] in test_word: 
                    is_chr_in_word(letter) 
                    if win_counter != len(set(test_word)): # if win counter == the number of unique char in the secret word, the game is over and user wins
                        win_counter += 1 
                        if win_counter == len(set(test_word)):
                            end(winner=True)

                else:
                    if lose_counter != 5: # if lose counter == 5, then the game is over, and user loses
                        lose_counter += 1
                    else:
                        end()
            
pygame.quit()
