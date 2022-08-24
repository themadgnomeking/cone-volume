#CHALLENGE
# You supervise a parking lot with 'n' parking spaces
# Yesterday you recordced whether each paring space was occupied by a car or was empty
# Today, you again record whether each parking space was occupied by a car or was empty
# Indicate the number of parking spaces that were occupied on both days

#INPUT
#  The input consists of 3 alines
#   * The first line contains integer n, the number of parking spaces. n is between 1 and 100
#   * The second line contains a string of n characters for yesterday's information, one char for each space
#       - A "C" indicates an occupied parking space (C for car), and a '.' indicates an empty parking space. 
#       - example: CC. means the first 2 parking spaces were occupied and the thrid was empty
#   * The third line contains a string of n characters for today's information, same format

#OUTPUT
# the number of spaces that were occupied on both days

def occupied_spaces(occupied, yesterday_result, today_result):
    
    occupied = 0

    for i in range(len(yesterday_result)):
        if yesterday_result[i] == 'C' and today_result[i] == 'C':
            occupied = occupied + 1
    return occupied

#test_case_01 = (10, "CC..CC..CC", "CC..CC..CC" )

print(occupied_spaces(10, "CC..CC..CC", "CC..CC..CC" )) # results is 6 and should be 12