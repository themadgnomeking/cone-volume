#original problem https://dmoj.ca/problem/coci08c1p2
# Adrian, Bruno and Goran wanted to join the bird lovers' club. However, they did not know that all applicants must pass an entrance exam. 
# The exam consists of  questions, each with three possible answers: ,  and .
# Unfortunately, they couldn't tell a bird from a whale so they are trying to guess the correct answers. 
# Each of the three boys has a theory of what set of answers will work best:
#   Adrian claims that the best sequence is: A, B, C, A, B, C, A, B, C, A, B, C, ...
#   Bruno is convinced that this is better: B, A, B, C, B, A, B, C, B, A, B, C, ...
#   Goran laughs at them and will use this sequence: C, C, A, A, B, B, C, C, A, A, B, B, ...

# Write a program that, given the correct answers to the exam, determines who of the three was right – 
# whose sequence contains the most correct answers.

#Input Specification
# * The first line contains an integer N(1 <= N <= 100), the number of questions on the exam. 
# * The second line contains a string of N letters A, B and C. These are, in order, the correct answers to the questions in the exam.

#Output Specification
# On the first line, output M , the largest number of correct answers one of the three boys gets. 
# After that, output the names of the boys (in alphabetical order) whose sequences result in M correct answers.

N = input()

adrian = "ABCABCABCABCABCABCABCABCABCABCABCABCABCABCABC"
bruno = "BABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABC"
goran = "CCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABB"



#compare N with adrian, count each instance of the letters in N show up, then compare bruno, and goran.
# print out the maximum amouunt of letters and print out the number and name


print(len(N))
#print(adrian[len(N)])


            

