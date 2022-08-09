# You'd like to register an account on an extremely entertaining website. 
# You've already selected a username, but it seems that the requirements for choosing a password are quite strict, 
# in order to completely protect your account from being hacked into. 
# The password must be a string between 8 and 12 characters long (inclusive), 
# such that every character is either a lowercase letter (a … z), uppercase letter (A … Z), or digit (0 … 9). 
# Furthermore, it must contain at least three lowercase letters, at least two uppercase letters, and at least one digit.

# You've got a potential password in mind, a non-empty string made up of at most  characters, 
# each of which is a lowercase letter, uppercase letter, or digit. 
# Rather than entering the password into the site and risking rejection, 
# you'd like to determine for yourself whether or not your password would validly satisfy all of the rules.

# INPUT
# The first and only line of input consists of a single string, the password.

# OUTPUT
# Output a single string, either Valid if the password is valid, or Invalid otherwise.
import string
import random


def uncrackable(string):

    psw_lngth = len(string)
    start_num = 8
    end_num = 12


    if  psw_lngth >= start_num and psw_lngth <= end_num:
        lower_char_count = 0
        upper_char_count = 0
        num_char_count = 0
        
        for char in string:
            
            if char.islower():
                lower_char_count += 1
            if char.isupper():
                upper_char_count += 1
            if char.isdigit():
                num_char_count += 1
        
        if lower_char_count >= 3 and upper_char_count >= 2 and num_char_count >= 1:
            return "Valid" 
        else:
            return "Invalid " 
    else:
        return "Invalid "
            

test_01 = "PassW0rd" #valid 8 char, 2 uppercase, 1 number
test_02 = "CorrectHorseBatteryStaple" # invalid too many char
test_03 = "passwIIId" #invalid no numbers
test_04 = "thisWillf41lbCau5et00M4nyChar" # invalid, too many chars
test_05 = "thisWWillf4" # valid


test_samples = [
    "PassW0rd",
    "CorrectHorseBatteryStaple",
    "passwIIId",
    "thisWillf41lbCau5et00M4nyChar",
    "thisWillf41lbC",
    "thisWWillf4",
    "orseBattery",
    "1rseBattery",
    "H3eBattery",
    "Ho5attery",
    "HorseBattery",
    "Hordtery",
    "HorseB422ry", 
    "Horss6tery"]

x = 0

for tests in test_samples:
    x += 1
    print("test " + str(x) + " " + uncrackable(tests))
    
#print(uncrackable(test_05))
#print(len(test_05))
#print(any(char.isdigit() for char in test_05))
#print(any(char.isupper() for char in test_05))
#rint(any(char.islower() for char in test_05))