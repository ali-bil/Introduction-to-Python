# Define an initializer for the Tile class, create a Tile object

# definition of a Tile class
class Tile:
    
    def __init__(self, number):
        self.number = number

    
# create two tiles with numbers 3 and 4   
my_tile = Tile(3)
your_tile = Tile(4)

    
###################################################
# Testing code

print (my_tile)
print (my_tile.number)
#print (your_tile)
#print (your_tile.number)

####################################################
# Output of testing code

# test 1
#<__main__.Tile object>
#3

# test 2
#<__main__.Tile object>
#4