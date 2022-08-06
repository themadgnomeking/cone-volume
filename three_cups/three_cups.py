#CHALLENGE
# There are three rows of opaque cups
#   * one at the left (location 1)
#   * one in the middle (location 2)
#   * one at the right (location 3)
#
# There is a ball under the cup at the left
# It's our job to keep track of the location of the ball as the cups gets swapped

# There are three types of swaps
#   A. Swap the left and middle cups
#   B. Swap the middle with the right cups
#   C. Swap the lft and right cups

# INPUT:
# one line of at most 50 characters. 
# Each character specifies a type of swap (A, B, or C)

# OUTPUT:
# 1. the ball is under the left cup
# 2. the ball is under the middle cup
# 3. the ball is under the right cup

def three_cups(cup_swap):
    
    location = 1

    for ball in cup_swap:
        if ball == 'A' and location == 1:
            location = 2
        elif ball == 'A' and location == 2:
            location = 1
        elif ball == 'B' and location == 2:
            location = 3
        elif ball == 'B' and location == 3:
            location = 2
        elif ball == 'C' and location == 1:
            location = 3
        elif ball == 'C' and location == 3:
            location = 1
        
    return location
    



#test cases
test_case_01 = 'ACAC'

print(three_cups(test_case_01))