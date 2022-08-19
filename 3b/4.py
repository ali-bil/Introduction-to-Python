# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.


import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
 

WIDTH = 400
HEIGHT = 400
radius = 1


# Timer handler
def tick():
    global radius
    radius += 1
    
# Draw handler
def draw_handler(canvas):
    canvas.draw_circle((HEIGHT // 2, WIDTH // 2), radius, 1, 'Orange','Orange')
# Create frame and timer   
frame = simplegui.create_frame('Testing', HEIGHT, WIDTH)
timer =  simplegui.create_timer(100, tick)

frame.set_draw_handler(draw_handler)
        
#Start timer
frame.start()
timer.start()
