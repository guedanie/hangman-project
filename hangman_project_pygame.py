import pygame, sys
from pygame.locals import *
import time
import pandas as pd
import numpy as np
pygame.init()

pygame.display.set_caption("Hangman")

win_height = 480  
win_width = 700

BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)

win_counter = 0
lose_counter = 0

def select_secret_word():
    words = pd.read_csv("word-meaning-examples.csv")
    random_sample = words.sample()
    index = random_sample.index
    random_sample = words.loc[index]
    random_sample = random_sample.values[0]
    test_word = random_sample[0].lower()
    return test_word, index

test_word_and_index = select_secret_word()
test_word = test_word_and_index[0].lower() 
index = test_word_and_index[1]

display_surface = pygame.display.set_mode((win_width, win_height))
hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'), pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'), pygame.image.load('hangman6.png')]

buttons = []
letters = "abcdefghijklmnopqrstuvwxyz" 
labels = []
guessed = []
dashes = "_" * len(test_word)


# Similar as the function above, this uses the index to pull the definition of the word
def return_meaning(index):
    words = pd.read_csv("word-meaning-examples.csv")
    random_sample = words.loc[index]
    random_sample = random_sample.values[0]
    meaning = random_sample[1].lower()
    return meaning




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

def intro():
    message("Howdy - wanna play a game of hangman?", 400, 100, 32)

def image():
    display_surface.blit(hangmanPics[0], (win_width // 3, win_height // 3))

def spaced_out_word(word):
    length = len(word)
    space_word = ["_"]
    space_word += (["_"] * length)
    string = ''
    return (string.join(space_word))

def draw_circle(x, y):
    pygame.draw.circle(display_surface, BLUE, (x, y), 15, 0)

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

    h = 300
    w = 400
    count = len(guessed) + 20
    # for i in guessed:
    #     pygame.draw.circle(display_surface, BLUE, (h + count, w), 15, 0)
    #     button_label(i, h + count, w)
    message(f"Guessed letters: {str(guessed)}", h, w, 30)

    pygame.display.update()  

def buttonHit(x, y):
    for i in range(len(buttons)):
        if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
            if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                return buttons[i][5]
    return None
        

def is_chr_in_word(letter):
    global dashes

    global letters

    correct_letter_index = [i for i in range(len(test_word)) if test_word.startswith(letters[letter], i)]

    dashes = list(dashes)
    for x in correct_letter_index:
        dashes[x] = letters[letter]
    dashes = ''.join(dashes)
    # dashes.replace(" ", "")
        
    
def end(winner=False):
    global index
    meaning = return_meaning(index)
    lostTxt = 'You Lost, press any key to play again...'
    winTxt = 'WINNER!, press any key to play again...'
    pygame.time.delay(1000)
    display_surface.fill(GREEN)

    if winner == True:
        label = winTxt
    else:
        label = lostTxt

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
    
def reset():
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
    
    



print(test_word)

create_circles()
    
create_label_list()

inPlay = True

while inPlay:
    
    
    draw_circles_and_labels()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            inPlay = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_position = pygame.mouse.get_pos()
            letter = buttonHit(click_position[0], click_position[1])
            if letter != None:
                buttons[letter][4] = False
                guessed.append(letters[letter])
                if letters[letter] in test_word:
                    is_chr_in_word(letter)
                    if win_counter != len(set(test_word)):
                        win_counter += 1
                        if win_counter == len(set(test_word)):
                            end(winner=True)

                else:
                    if lose_counter != 5:
                        lose_counter += 1
                    else:
                        end()
            
pygame.quit()
