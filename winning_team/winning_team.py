#output a message that depends on the outcome of a basketball game

#In baskeball, three plays score points:
#   a three point shot
#   a two point shot
#   a one point free throw

def basketball_score(b_list):
    team_01 = []
    team_02 = []

    #team_01_score = ((team_01[0] * 3) + (team_01[1] * 2) + (team_01[2]))
    #team_02_score = (team_02[0] * 3) + (team_02[1] * 2) + (team_02[2])

    count = 0

    for score_b in b_list:
        if count < 3:
            team_01.append(score_b)
            count += 1
        else:
            team_02.append(score_b)
            count += 1

    team_01_score = (team_01[0] * 3) + (team_01[1] * 2) + (team_01[2])
    team_02_score = (team_02[0] * 3) + (team_02[1] * 2) + (team_02[2])
    
    if team_01_score > team_02_score:
        return "Apples Win: " + str(team_01_score)
    elif team_01_score < team_02_score:
        return "Banana's Win: " + str(team_02_score)
    elif team_01_score == team_02_score:
        return "It's a tie."

    #team_01_score = (team_01[0] * 3) + (team_01[1] * 2) + (team_01[2])
    #team_02_score = (team_02[0] * 3) + (team_02[1] * 2) + (team_02[2])

    #return team_02_score

test_case_01 = [5, 1, 3, 1, 1, 3]
test_case_02 = [1, 1, 3, 5, 1, 3]
test_case_03 = [1, 1, 1, 1, 1, 1]

print(basketball_score(test_case_03))