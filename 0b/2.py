# Compute the number of seconds in a given number of hours, minutes, and seconds.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
hours = 7
minutes = 21
seconds = 37


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
hours = 10
minutes = 1
seconds = 7
###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter formula on the next line.
total_seconds=(hours*60+minutes)*60+seconds


###################################################
# Test output
# Student should not change this code.

print (str(hours) , " hours, " , str(minutes) , " minutes, and",str(seconds) , " seconds. Total " , str(total_seconds) , " seconds.")

