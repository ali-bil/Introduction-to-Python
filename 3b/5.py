# Reflex tester

###################################################
# Student should add code where relevant to the following.


import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
 

total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks
    total_ticks += 1
    
# Button handler
def click():
    global first_click,total_ticks
    if first_click:
        total_ticks = 0
        first_click = False
        timer.start()
    else:
        timer.stop()
        first_click = True
        print (total_ticks/100.0 ,"seconds between click")
        total_ticks = 0

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
 