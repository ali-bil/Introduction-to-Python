# Display "This is easy?"

###################################################
# Student should add code where relevant to the following.


import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
 

# Draw handler
def draw(canvas):
    canvas.draw_text("This is easy?" , [90, 100], 49, "Red")

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("This is easy", 400, 200)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()

