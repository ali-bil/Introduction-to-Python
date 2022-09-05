# Define a getter method for the Tile class


# definition of a Tile class
class Tile:
    
    # definition of intializer
    def __init__(self, num):
        self.number = num
        
    # definition of getter for number
    def get_number(self):
        return self.number
    
# create a Tile called my_tile with number 3    
my_tile = Tile(3)
tile_number = my_tile.get_number()
  
    
###################################################
# Testing code

print (my_tile)
print (tile_number)


####################################################
# Output of testing code

#<__main__.Tile object>
#3