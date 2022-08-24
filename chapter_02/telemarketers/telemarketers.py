#CHALLENGE
#a phone number belonging to a telemarketer has the following
#   * first digit is 8 or 9
#   * forth digit is 8 or 9
#   * second and third digit are the same
#
# Input: 
#   four lines of input
#       these are the first, second, third, and forth diigits of the number re spectively
#       each digit is an integer between 0 and 9
# Output:
#   if number belongs to a telemarketer: IGNORE
#   else output answer

def identify_telemarketer():
    num_one = int(input("first number: "))
    num_two = int(input("second number: "))
    num_three = int(input("thrid number: "))
    num_four = int(input("fourth number: "))

    if (num_one == 8 or num_one == 9) and (num_two == num_three) and (num_four == 9 or num_four == 8):
        return "Ignore this number"
    else:
        return str(num_one) + str(num_two) + str(num_three) + str(num_four)

print(identify_telemarketer())