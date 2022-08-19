# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below


import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

count = 0
# Define event handlers for four buttons
def reset():
    global count
    count = 0
    
def decrement():
    global count
    count -= 1
    
def increment():
    global count
    count += 1
    
def print_count():
    print (count)

    
# Create frame and assign callbacks to event handlers

frame = simplegui.create_frame("chande count", 200, 200)

frame.add_button("Reset", reset)
frame.add_button("Increment", increment)
frame.add_button("Decrement", decrement)
frame.add_button("Print count", print_count)

# Start the frame animation

frame.start()

    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Expected output from test

#1
#2
#-2
