#https://dmoj.ca/problem/ccc02j2

# Americans spell differently from Canadians. 
# Americans write 'neighbor' and 'color' while Canadians write 'neighbour' and 'colour'. 
# Write a program to help Americans translate to Canadian.

# Your program should interact with the user in the following way. 
# The user should type a word (not to exceed 64 letters) and if the word appears to use 
# American spelling, the program should echo the Canadian spelling for the same word. 
# If the word does not appear to use American spelling, it should be output without change. 
# When the user types quit! the program should terminate.

# The rules for detecting American spelling are quite naive: 
# If the word has more than four letters and has a suffix consisting of a consonant followed by or,
# you may assume it is an American spelling, 
# and that the equivalent Canadian spelling replaces the or by our. 
# Note: you should treat the letter y as a vowel.

cur_word = str(input("Please type your word (limit 64 characters): "))

if len(cur_word) <= 64:
    if len(cur_word) >= 4:
        #print("larger than or equal to 4")
        #print(new_word[-2:])
        if cur_word[-2:] == 'or':
            new_word = cur_word[:-2] + 'our'
            print(new_word)
        else:
            print(cur_word)
else:
    print("Please limit your characters to 64 or less!")
    cur_word = str(input("Please type your word (limit 64 characters): "))