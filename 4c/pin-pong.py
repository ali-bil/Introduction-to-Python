  # Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1,score2=0,0
paddle1_pos,paddle1_vel=0,0
paddle2_pos,paddle2_vel=0,0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
# define event handlers for buttons; "Start", "Stop", "Reset"
def reset():
    global score1,score2
    score1,score2=0,0
    new_game()
    
def spawn_ball(direction):

    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH//2,HEIGHT//2]
    ball_vel =[0,0]
    if direction:
        ball_vel[0] += random.randrange(2, 4)
    else:
        ball_vel[0] -= random.randrange(2, 4)
    ball_vel[1] -= random.randrange(2, 5)


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(False)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
     
    # draw mid line and gutters
    canvas.draw_text(str(score1)+"/"+str(score2),( 450,70), 50, 'White')
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "Red")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "Blue")
        
    # update ball
    if ball_pos[1]< BALL_RADIUS and ball_pos[0]>PAD_WIDTH and ball_pos[0]<WIDTH-PAD_WIDTH :
        ball_vel[1] = -ball_vel[1] 
 
    if ball_pos[1]> HEIGHT-BALL_RADIUS and ball_pos[0]>PAD_WIDTH and ball_pos[0]<WIDTH-PAD_WIDTH : 
        ball_vel[1] = -ball_vel[1] 
        
    if ball_pos[0] > WIDTH - PAD_WIDTH:
        score1 += 1
        spawn_ball(LEFT)
         
        
    if ball_pos[0] < PAD_WIDTH:
        score2 += 1
        spawn_ball(RIGHT)
 
    if ball_pos[0] < BALL_RADIUS and ball_pos[1] >  paddle2_pos and ball_pos[1] < paddle2_pos+PAD_HEIGHT :
        ball_vel[0] = -ball_vel[0]*1.1
        ball_pos[0] = BALL_RADIUS
         
       
    if ball_pos[0] > WIDTH-(BALL_RADIUS) and ball_pos[1] > paddle1_pos and ball_pos[1] < paddle1_pos+PAD_HEIGHT :
        ball_vel[0] = -ball_vel[0]*1.1
        ball_pos[0] = WIDTH-BALL_RADIUS
         

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    
    if paddle1_pos + paddle1_vel <= HEIGHT-PAD_HEIGHT and paddle1_pos + paddle1_vel >= 0:
        paddle1_pos+=paddle1_vel
        
    if paddle2_pos + paddle2_vel <= HEIGHT-PAD_HEIGHT and paddle2_pos + paddle2_vel >= 0:
        paddle2_pos+=paddle2_vel
       
    
     # draw paddles
    canvas.draw_line([0, paddle2_pos+PAD_WIDTH],[0, paddle2_pos+PAD_HEIGHT], 20, "White")
    canvas.draw_line([WIDTH, paddle1_pos+PAD_WIDTH],[WIDTH,paddle1_pos+PAD_HEIGHT], 20, "White")
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel,paddle2_pos
    if key == simplegui.KEY_MAP["up"] and paddle1_pos > 0:
        paddle1_vel = -5
    if key == simplegui.KEY_MAP["down"]and paddle1_pos < HEIGHT:
        paddle1_vel = 5
        
    if key == simplegui.KEY_MAP["w"]and paddle2_pos > 0:
        paddle2_vel = -5
    if key == simplegui.KEY_MAP["s"]and paddle2_pos < HEIGHT:
        paddle2_vel = 5
        


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle2_vel = 0

    
 
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button('reset', reset)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
