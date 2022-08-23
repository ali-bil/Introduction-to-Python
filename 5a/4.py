# String list joining problem
def string_list_join(list):
    string = str()
    for element in list:
        string += element
    return string

###################################################
# Test data

print (string_list_join(["pig", "dog"]))
#print (string_list_join(["spam", " and ", "eggs"]))
#print (string_list_join(["a", "b", "c", "d"]))


###################################################
# Output

#pigdog
#spam and eggs
#abcd