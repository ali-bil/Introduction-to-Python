# Mini-project #6 - Blackjack

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

 

# initialize some useful global variables
in_play = False
score = 0
hand_text  = "hit or stand?"
dealer_text = ""
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: "), suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        hand = ""
        for card in self.cards:
            hand = hand + str(card) + " "
        return "Hand contains " + hand
    
    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
 
        for card in self.cards:
            if card.get_rank() in  VALUES:
                value += VALUES[card.get_rank()]
                if 'A' == card.get_rank() and value + 10 <= 21:
                     value += 10
        return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards  
        i=10
        for card in self.cards:
            card.draw(canvas, [pos[0]+i,pos[1]])
            i+=90
            
 
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object

        self.cards = []
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(suit + rank)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        card = self.cards.pop()
        return Card(card[0],card[1])
    
    def __str__(self):
        # return a string representing the deck
        deck = ""
        for card in self.cards:
            deck = deck + str(card) + " "
        return "Deck contains " + deck



#define event handlers for buttons
def deal():
    global in_play, dealer, hands, deck, hand_text, dealer_text,score
    # your code goes here
    if in_play: 
        score -= 1
    hand_text  = "Hit or stand?"
    dealer_text = ""
    dealer = Hand()
    hands = Hand()
    deck = Deck()
    deck.shuffle()
    dealer.add_card(deck.deal_card())
    hands.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    hands.add_card(deck.deal_card())
    in_play = True

def hit():
    global hands, deck, hand_text,dealer_text, score, in_play
    if not in_play: 
        return
    if hands.get_value() <= 21 :
        hands.add_card(deck.deal_card())
        
        if hands.get_value() > 21 :
            dealer_text ='You have busted and lose'
            hand_text = 'New deal?'
            score -= 1
            in_play = False
         
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global hands, dealer, deck,dealer_text, hand_text,score,in_play
    if not in_play: 
        return

    while dealer.get_value()<17:
        dealer.add_card(deck.deal_card())
    if dealer.get_value() > 21 :
            dealer_text = 'dealer lost'  
            hand_text = 'New deal?'
            score += 1
    elif dealer.get_value() >= hands.get_value():
        dealer_text = 'player lose'
        hand_text = 'New deal?'
        score -= 1
    else:
        dealer_text = 'player win'
        hand_text = 'New deal?'
        score += 1
    in_play = False
# draw handler    
def draw(canvas):
           # test to make sure that card.draw works, replace with your code below
    canvas.draw_text(hand_text, (250, 400), 30, 'White')
    canvas.draw_text(dealer_text, (250, 150), 30, 'White')
    canvas.draw_text('dealer', (100, 150), 30, 'White')
    canvas.draw_text('player', (100, 400), 30, 'White')
    canvas.draw_text('score: '+str(score), (400, 70), 30, 'White')

    dealer.draw(canvas, [100, 200])
    hands.draw(canvas, [100, 450])
    canvas.draw_text('Blackjack', (100, 50), 30, 'White')
    if in_play:
        pos=[145, 248]
        card_back_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1] )
        canvas.draw_image(card_back, card_back_loc, CARD_BACK_SIZE, pos, CARD_BACK_SIZE)
      
    #hand_text dealer_text
dealer = Hand()
hands = Hand()
deck = Deck()
# initialization frame
frame = simplegui.create_frame("Blackjack", 800, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


