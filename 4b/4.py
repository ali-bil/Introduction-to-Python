# Ball radius control - version 2

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

WIDTH = 300
HEIGHT = 200
ball_radius = 10
ball_growth = 0
BALL_GROWTH_INC = .2

# Handlers for keydown and keyup
def keydown(key):
    global ball_growth
    if key == simplegui.KEY_MAP["up"]:
        ball_growth = BALL_GROWTH_INC
    if key == simplegui.KEY_MAP["down"] and ball_radius > BALL_GROWTH_INC:
        ball_growth = -BALL_GROWTH_INC
    # add code here

def keyup(key):
    global ball_growth
    if key == simplegui.KEY_MAP["up"]:
        ball_growth = 0
    if key == simplegui.KEY_MAP["down"]:
        ball_growth = 0
 
    
    
# Handler to draw on canvas
def draw(canvas):
    global ball_radius
    if ball_radius >= BALL_GROWTH_INC:
        ball_radius += ball_growth
    else:
        ball_radius += BALL_GROWTH_INC
   
    print  (ball_radius)
    # note that CodeSkulptor throws an error if radius is not positive
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], ball_radius, 1, "White", "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
