# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
 

counter = 0

# Timer handler
def tick():
    global counter
    print (counter)
    counter += 1
    
# Event handlers for buttons    
def reset():
    global counter
    counter = 0
    
def start():
    timer.start()  
    
def stop():
    timer.stop()
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(1000, tick)
frame.add_button('reset', reset)
frame.add_button('start', start)
frame.add_button('stop', stop)

# Start timer and frame
frame.start()
timer.start()
