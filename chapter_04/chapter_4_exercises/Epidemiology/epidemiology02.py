P = int(input())
N = int(input())
R = int(input())

infected_count = N
people_count = N

day = 0
while True:
    people_count = people_count + (infected_count * R)
    infected_count = infected_count * R
    day += 1
    if people_count >= P:
        if people_count == P:
            print(day + 1)
        else:
            print(day)
        break