# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

# Functions that compute RPSLS
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else :
        return "not correct name"

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else :
        return "not correct number"
def rpsls(player_choice): 
    #Player chooses rock
    #Computer chooses scissors
    #Player wins!
    print
     # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    if player_number in range(5):
        # print a blank line to separate consecutive games
        
        # print out the message for the player's choice
        print ("Player chooses "+player_choice)
        
        # compute random guess for comp_number using random.randrange()
        comp_number = random.randrange(0,5)
        
        # convert comp_number to comp_choice using the function number_to_name()
        comp_choice = number_to_name(comp_number)
        
        # print out the message for computer's choice
        print ("Computer chooses "+comp_choice  )
        
        # compute difference of comp_number and player_number modulo five
        difference = (comp_number - player_number)%5
        # use if/elif/else to determine winner, print winner message
        if difference == 1 or difference == 2 :
            print ("Computer wins!")
        elif difference == 3 or difference == 4 :
            print ("Player wins!")
        elif difference == 0:
            print( "Player and computer tie!")
        else:
            print ("not correct difference")
    else: 
            print ("Error: Bad input "+player_choice+" to rpsls")
   
    
# Handler for input field
def get_guess(guess):
    rpsls(guess)
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
