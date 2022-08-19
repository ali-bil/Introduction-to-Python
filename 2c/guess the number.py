# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
 
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global count, maxN,minN,secret_number
    count,minN = 0,0
    input_guess


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global count, maxN,minN,secret_number
    print()
    print ("Range is [0,100)")
    count = 7 
    minN = 0
    maxN = 99
    secret_number =  random.choice(range(minN,maxN))
    print ("Number of remaining guesses is ",count)
    input_guess
     

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global count, maxN,minN,secret_number
    print
    print ("Range is [0,1000)")
    count = 10
    minN = 0
    maxN = 999
    secret_number =  random.choice(range(minN,maxN))
    print ("Number of remaining guesses is ",count)
    input_guess
    
    
def input_guess(guess):
    # main game logic goes here	
    global count, maxN,minN,secret_number
    
    print
    if count > 0:
        count -= 1
        print( "Guess was "+guess)
        print ("Number of remaining guesses is ",count)
        guess = int(guess)
        if guess > maxN or guess < minN:
            print ("out of range")
        else:
            if guess > secret_number:
                print ("Lower!")
            elif  guess < secret_number:
                print ("Higher!")
            else:
                print ("Correct!")
        
    else:
        print( "You ran out of guesses.  The number was ", secret_number)
    
# create frame

frame = simplegui.create_frame("Game", 100, 200)
frame.add_button("Range is [0,100)", range100)
frame.add_button("Range is [0,1000)", range1000)
frame.add_input("Enter a guess", input_guess, 100)
# register event handlers for control elements and start frame
 
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
