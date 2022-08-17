import simplegui
# template for "Stopwatch: The Game"

# define global variables
seconds = 0
stopwatch = "0:00.0"
total_stops = 0
stops = 0
WIDTH = 400
HEIGHT = 400
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t % 10000 / 1000
    B = t % 1000 / 100
    C = t % 100 / 10
    D = t % 10
    
    return str(A)+":"+str(B)+str(C)+"."+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def reset():
    if timer.is_running():
        timer.stop()
    global seconds,stopwatch,total_stops,stops
    seconds = 0
    stopwatch = "0:00.0"
    total_stops = 0
    stops = 0
    
def start():
    timer.start()  
    
def stop():
    global total_stops,stops
    if timer.is_running():
        if  stopwatch[-1] == "0" :
            stops += 1
        timer.stop()
        total_stops += 1
    

#define event handler for timer with 0.1 sec interval
def tick():
    global seconds,stopwatch
    seconds += 1
    stopwatch = format(seconds)
    

# define draw handler

def draw_handler(canvas):
    pricol = str(stops)+"/"+str(total_stops)
    canvas.draw_text(stopwatch, (HEIGHT//2.5,WIDTH//2), 50, 'Gray', 'serif')
    canvas.draw_text(pricol, (HEIGHT-0.2*HEIGHT,WIDTH-0.8*WIDTH), 50, 'Red', 'serif')


 
 
 
frame = simplegui.create_frame("Stopwatch", HEIGHT, WIDTH)
frame.set_draw_handler(draw_handler)

frame.add_button('reset', reset)
frame.add_button('start', start)
frame.add_button('stop', stop)
timer = simplegui.create_timer(100, tick)
# start frame
frame.start()
