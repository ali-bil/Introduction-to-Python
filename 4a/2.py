# List reference problem

###################################################
# Student should enter code below

a = [5, 3, 1, -1, -3, 5]
b = a
b[0] = 0

print a
print b

###################################################
# Explanation
''' 
The first element of list a is changed because the string "b = a"
means that b refers to list a, so the two lists refer to the first list.
So if b[0] = 0 then a[0] == 0
'''
