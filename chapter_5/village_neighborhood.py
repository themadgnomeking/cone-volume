# https://dmoj.ca/problem/ccc18s1
# CCC '18 S1 - Voronoi Villages

#CHALLENGE
# There are 'n' villages located at distinct points on a striaght road
# Each village is preresented by an integer that indicates its position on the road.
# A village's left neighbor is the village with the next smalles position;
# a village's right neighbor is the village with the next biggest position.
# The left neighbor, plus half the space between the village and its right neighbor.
# For example, if there's a village at position 10,with its left neighbor at position 6 and its right neighbor at position 15,
# then this villages neighborhood starts from position 8 (halfway between 6 and 10) and ends at position 12.5 (halfway between 10 and 15)
# The leftmost and rightmost villages have only one neighbor, so the definition of a neighborhood doesn't make sense for them.
# We'll ignore the neighborhoods of those two villages in this problem.
# The "SIZE" of a neighbor is calculated as the neighborhood's right position minus the neighborhood's leftmost position.
# For example, the neighborhood that goes from 8 to 12.5 has size 12.5 - 8 = 4.5.
# Determine the size of the smallest neighborhood

#INPUT
# The input consists of the following lines:
#   * A line containing integer 'n', the number of villages. 'n' is between 3 and 100
#   * 'n' lines, each of which gives the position of a village. Each position is an integer between -1,000,000,000 and 1,000,000,000.
#       The positions need not come in order from left to right; 
#       the neighbor of a village could be anywhere in these lines

#OUTPUT
# Output the size of the smallest neighborhood. Include exactly one digit after the decimal point.

num_villages = int(input())
village_positions = []

for i in range(num_villages):
    village_positions.append(int(input()))

village_positions.sort()

left_village = (village_positions[1] - village_positions[0])/2
right_village = (village_positions[2] - village_positions[1])/2
min_village_size = left_village + right_village

for i in range(2, num_villages-1):
    left_village = (village_positions[i] - village_positions[i - 1])/2
    right_village = (village_positions[i + 1] - village_positions[i])/2
    size = left_village + right_village
    if size < min_village_size:
        min_village_size = size

print(size)