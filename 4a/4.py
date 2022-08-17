# Vector addition function

###################################################
# Student should enter code below
def add_vector(*list):
    return [list[0][0]+list[1][0],list[0][1]+list[1][1]]



###################################################
# Test

print add_vector([4, 3], [0, 0])
print add_vector([1, 2], [3, 4])
print add_vector([2, 3], [-6, -3])



###################################################
# Output

#[4, 3]
#[4, 6]
#[-4, 0]

