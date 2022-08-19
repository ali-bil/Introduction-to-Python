# Echo an input field

###################################################
# Student should add code where relevant to the following.

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# Handlers for input field

def get_input(inp):
    print (inp)
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)
frame.add_input("Input", get_input, 100)

# Start the frame animation

frame.start()


###################################################
# Test

get_input("First test input")
get_input("Second test input")
get_input("Third test input")

###################################################
# Expected output from test

#First test input
#Second test input
#Third test input
