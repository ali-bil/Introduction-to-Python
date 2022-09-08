# "Guess the number" mini-project

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


# define global variables
range = 100
secret_number = 0
def new_game():
    # initialize global variables used in your code here
    global secret_number, max_guesses,count_guesses,guesses_remaining
    secret_number = random.randrange(0, range)
    count_guesses = 1
    if range == 100:
        max_guesses = 7
    else:
        max_guesses = 10
    guesses_remaining = max_guesses
    print ("New game. Range is from 0 to", range)
    print ("Number of remaining guesses is", max_guesses)
 
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range = 1000
    new_game()
  
def input_guess(guess):
    # main game logic goes here	
    global count_guesses, inp
  

    try:
            guess_num = int(guess)
            print("Guess №" + str(count_guesses) + " out of " + str(max_guesses) + " was " + guess)
            guess_num = int(guess)
             
    except ValueError:
            print("Error! Not number")
            return
    except NameError:
            print("Error! Press button please")
            return
    

    #inp.set_text("") нужно вернуть каретку на начало строки (не знаю как)
     
    if guess_num > range or guess_num < 0:
            print("Out of range")
            return
 
    if guess_num == secret_number:
        print("You guessed it!\n")
        new_game()
    else:
        count_guesses += 1
        if count_guesses <= max_guesses:
            if guess_num > secret_number:
                print("Enter a lower number.")
            elif guess_num < secret_number:
                print("Enter a higher number.")
        else:
            print("Secret number :",secret_number,". Game over. \n")
            new_game()
 
# create frame

frame = simplegui.create_frame("Game", 100, 200)
frame.add_button("Range is [0,100)", range100)
frame.add_button("Range is [0,1000)", range1000)
inp = frame.add_input("Enter a guess", input_guess, 100)

# start frame
frame.start()
 
 