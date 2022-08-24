#CHALLENGE
# Pero has a data plan with his cell phone provider that offers him x megabytes of data per month.
#In addition, any data he doesn't use in a given month carries over to the next month.
#For example, if x is 10 and Pero uses only 4MB iin a given month, the remaining 6MB carry over to the next month totaling 16MB availalbe
#we're given the number of megabytes of data that Pero uses in each of the first n months. 
#Our task is to determine the number of megabytes available for the following month

#INPUT
# The input consists of the following lines:
#   * a line containing integer x, the number of megabytes given to Pero per month
#     x is between 1 and 100

#   * a line containing integer n, the number of months that Pero has had the data plan.
#     n is between 1 and 100

#   * n lines, one for each month, giving the integer number of megabytes that Pero uses in that month.
#     Each number is at least 0 and will never outstrip the number of available megabytes.
#     (For example, if x is 10 and Pero has 30MB available, the next number will be at most 30)

#OUTPUT
#the number of megabytes available for the next month

mb_per_month = int(input())
n = int(input())

total_mb = mb_per_month * (n + 1)

for i in range(n):
    used = int(input())
    total_mb = total_mb - used

print(total_mb)