# Counter ticks

###################################################
# Student should add code where relevant to the following.

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
 
counter = 0

# Timer handler
def tick():
    global counter
    print (counter)
    counter += 1

# create timer
timer = simplegui.create_timer(1000, tick)

timer.start()

