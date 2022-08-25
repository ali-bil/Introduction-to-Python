# implementation of card game - Memory

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


image = simplegui.load_image("https://moigoroskop.org/images/karty/rubashka.png")

MAP_WIDTH = 190
MAP_HEIGHT = 300

# Canvas size
CAN_WIDTH = MAP_WIDTH / 2
CAN_HEIGHT = MAP_HEIGHT / 2

flag=False
# helper function to initialize globals
def new_game():
    global deck,indexx,click,open_card_index,turns,label
    deck = [str(i) for i in range(8)] * 2
    random.shuffle(deck) 
    indexx,open_card_index = [], []
    click,turns = 0, 0
    label.set_text("Turns = "+str(turns))
     
# define event handlers
def mouseclick(pos):
    global flag, deck,indexx,click,open_card_index,turns,label
    
    if click == 0:
        
        for i in range(len(deck)):
            if pos[0] >= i * CAN_WIDTH and pos[0] <= (i + 1) * CAN_WIDTH:
                indexx.append(i)
        click = 1

    elif click == 1:
        
        for i in range(len(deck)):
            if pos[0] >= i * CAN_WIDTH and pos[0] <= (i + 1) * CAN_WIDTH :
                if i not in indexx and i not in open_card_index:
                    indexx.append(i)
                    flag = True
                    click += 1
                    turns += 1
                    break
                else:
                    flag = False
                    
        if flag and deck[indexx[0]] == deck[indexx[1]] and indexx[0] not in open_card_index and indexx[1] not in open_card_index:
                    open_card_index.append(indexx[0])
                    open_card_index.append(indexx[1])
        
    else:
        
        for i in range(len(deck)):
            if pos[0] >= i * CAN_WIDTH and pos[0] <= (i + 1) * CAN_WIDTH and i not in indexx and i not in open_card_index:
                indexx = []
                indexx.append(i)  
                click -= 1    

    label.set_text("Turns = " + str(turns))         
           
def draw(canvas):
    global deck,indexx,click,open_card_index,turns
    for index in range(len(deck)):
        canvas.draw_text(deck[index], (MAP_HEIGHT / 3.2 * index + MAP_HEIGHT / 8, MAP_HEIGHT / 3), MAP_HEIGHT / 4.8, 'White')
        if index not in indexx  and index not in open_card_index :
            canvas.draw_image(image, [MAP_WIDTH / 2, MAP_HEIGHT / 2], [MAP_WIDTH, MAP_HEIGHT], 
                [CAN_WIDTH // 2 * index * 2 + 52, CAN_HEIGHT // 2], [CAN_WIDTH - 7, CAN_HEIGHT])
        
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", MAP_WIDTH * 8, MAP_HEIGHT / 2)
frame.add_button("Reset", new_game)
 
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
label = frame.add_label("Turns = 0")

# get things rolling
new_game()
frame.start()




# Always remember to review the grading rubric