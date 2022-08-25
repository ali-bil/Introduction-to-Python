# Challenge


import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# global constants
WIDTH = 1200
HEIGHT = 675
center = [WIDTH / 2, HEIGHT / 2]

# load test image
sea_image_size = [WIDTH, HEIGHT]
sea_image_center = [sea_image_size[0] / 2, sea_image_size[1] / 2]
sea_image =  simplegui.load_image("https://i0.wp.com/oceanblueproject.org/wp-content/uploads/2021/06/corolla-beach-north-carolina.jpg?resize=1200%2C675&ssl=1")

    
# draw handler
def draw(canvas):
     canvas.draw_image(sea_image, sea_image_center, sea_image_size, center, sea_image_size)

       
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)


# start frame
frame.start()                         