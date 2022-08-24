#People who study epidemiology use models to analyze the spread of disease. In this problem, we use a simple model.

#When a person has a disease, they infect exactly 'R' other people but only on the very next day. 
# No person is infected more than once. We want to determine when a total of more than 'P' people have had the disease.

#(This problem was designed before the current coronavirus outbreak, and we acknowledge the distress currently being 
# experienced by many people worldwide because of this and other diseases. We hope that including this problem at this 
# time highlights the important roles that computer science and mathematics play in solving real-world problems.)

#Input Specification
#There are three lines of input. Each line contains one positive integer. 
#   * The first line contains the value of 'P'. 
#   * The second line contains 'N', the number of people who have the disease on Day 0. 
#   * The third line contains the value of 'R'. Assume that P <= 10^7 and N <= P and R <= 10.

#Output Specification
#Output the number of the first day on which the total number of people who have had the disease is greater than 'P'.

def epid_caluclation(p, n, r):
    
    total_infected = 0 
    infected_count = n
    day = 0

    while total_infected < p: #total infected is less than the target number
        if infected_count == 1:
            total_infected = infected_count + r
            infected_count = r
        elif infected_count > 1:
            total_infected += infected_count * r
            infected_count = infected_count * r
        day += 1
    return day




print(epid_caluclation(10, 2, 1))