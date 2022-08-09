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

def uncrackable(string):

    psw_lngth = len(string)

    if psw_lngth >= 8 and psw_lngth <= 12:
        if (any(char.isdigit() for char in string)):
            if (any(char.isupper() for char in string)):
                if (any(char.islower() for char in string)):
                    return "valid"
    else:
        return "invalid"

test_01 = "PassW0rd"
test_02 = "CorrectHorseBatteryStaple"


print(uncrackable(test_02))