#CHALLENGE
# Martha goes to a casino and brings n quarters. The casino has three slot machines,
# and she plays them in order until she has no quarters left.
# That is, she plays the first slot machine, then the second, then the thrid, then back to the first,
# then the second, and so on. Each play costs one quarter

# The slot machine operate according to the following rules:
#   * The first slot machine pays 30 quarters every 35th time it is played
#   * The second slot machine pays 60 uarters every 100th time it is played
#   * The third slot machine pays 9 quarters every 10th time it is played
#   * no other plays pay anything.
# Determine the number of times Martha plays before she has no quarters left

#INPUT
# The input consists of four lines.
#   * The first line contains an integer n, the number of quarters that Martha brings to the casino. n is between 1 and 1000
#   * The second line contains an integer indicating the number of times that the first slot machine has played since it last paid
#     These plays occurred prior to Martha arriving, and Martha's plays continue from there.
#     For example, suppose that the first slot machine has been played 34 times since it last paid. 
#     Then, Martha will win 30 quarters the first time she plays
#   * The third line contains an integer indicating the number of times that the second slot machine has been played since it last paid.
#   * The fourth line contains an integer indicating the number of times that the third slot machine has been played since it last paid.

#OUTPUT
# Output the following sentence, where x is the number of times Martha plays before she has no quarters left:
# "Martha plays x times before going broke"

def going_broke():
    num_quarters = int(input("What is the starting quarter count? "))
    slot_1_plays = int(input("How many plays are in slot 1? "))
    slot_2_plays = int(input("How many plays are in slot 2? "))
    slot_3_plays = int(input("How many plays are in slot 3? "))

    plays = 0
    play_count = 1

    slot_1_cycle = 35
    slot_2_cycle = 100
    slot_3_cycle = 10

    slot_1_payout = 30
    slot_2_payout = 60
    slot_3_payout = 9

    while num_quarters != 0:
        
        if play_count == 1:
            num_quarters -= 1
            slot_1_plays += 1
            if slot_1_plays == slot_1_cycle:
                num_quarters += slot_1_payout
                play_count += 1
                plays += 1
            else:
                play_count += 1
                plays += 1
        elif play_count == 2:
            num_quarters -= 1
            slot_2_plays += 1
            if slot_2_plays == slot_2_cycle:
                num_quarters += slot_2_payout
                play_count += 1
                plays += 1
            else:
                play_count += 1
                plays += 1
        elif play_count == 3:
            num_quarters -= 1
            slot_3_plays += 1
            if slot_3_plays == slot_3_cycle:
                num_quarters += slot_3_payout
                play_count = 1
                plays += 1
            else:
                play_count = 1
                plays += 1

        
    return plays

    #while quarter count not equal to 0 - PLAY


print(going_broke())