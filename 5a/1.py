 # Echo mouse click in console

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# intialize globals
WIDTH = 450
HEIGHT = 300

# define event handler for mouse click, draw
def click(pos):
    print("Mouse click at " + str(pos))

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)

# start frame
frame.start()
  

 