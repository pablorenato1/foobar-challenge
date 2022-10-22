# Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

# Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

# Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

# For example, consider the matrix m:
# [
#   [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
#   [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
#   [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
#   [0,0,0,0,0,0],  # s3 is terminal
#   [0,0,0,0,0,0],  # s4 is terminal
#   [0,0,0,0,0,0],  # s5 is terminal
# ]
# So, we can consider different paths to terminal states, such as:
# s0 -> s1 -> s3
# s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
# s0 -> s1 -> s0 -> s5
# Tracing the probabilities of each, we find that
# s2 has probability 0
# s3 has probability 3/14
# s4 has probability 1/7
# s5 has probability 9/14
# So, putting that together, and making a common denominator, gives an answer in the form of
# [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
# [0, 3, 2, 9, 14].
# -- Python cases --
# Input:
# solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
# Output:
#     [7, 6, 8, 21]

# Input:
# solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# Output:
#     [0, 3, 2, 9, 14]

test = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

from fractions import Fraction
from fractions import gcd

def fraction(numerator, denominator=1):
    return 0 if numerator == 0 else Fraction(numerator, denominator)

def identity(m):
    return [[1 if i == e else 0 for e in range(m)] for i in range(m)]

def sub(i, q):
    return [[i[e][p]-q[e][p] for p in range(len(q))] for e in range(len(q))]

def mult(f, r):
    matrix = [[0 for e in i] for i in r]
    for p, i in enumerate(r):
        for p2, j in enumerate(i):
            for x in range(len(r)):
                matrix[p][p2] += r[x][p2]*f[p][x]     
    return matrix

def invert(a):
    b = identity(len(a))
    for d in range(len(a)):
        to1 = fraction(1, a[d][d])
        for j in range(len(a)):
            a[d][j] *= to1
            b[d][j] *= to1
        for i in range(len(a))[0:d] + range(len(a))[d + 1 :]:
            to0 = a[i][d]
            
            for j in range(len(a)):
                a[i][j] = a[i][j] - to0 * a[d][j]
                b[i][j] = b[i][j] - to0 * b[d][j]
    return b

def lcm(li):
    for p, i in enumerate(li):
        lcm = i if p == 0 else lcm * i // gcd(lcm, i)
    return lcm

def solution(m):

    terminal = [not any(row) for row in m]

    if terminal.count(True) == 1:
        return [1, 1]
    q = []
    r = []
    for z in terminal:
        if z == False:
            r.append([])
            q.append([])
    p = m[:]
    for pos, i in enumerate(terminal):
        if i == True:
            continue
        s = sum(m[pos])
        for pos2, j in enumerate(m[pos]):
            m[pos][pos2] = fraction(j, s)
    fff = 0
    for pos, z in enumerate(terminal):
        if z == False:
            for pos2, u in enumerate(m[pos]):
                if terminal[pos2]:
                    r[fff].append(u)
                    continue
                q[fff].append(u)
            fff += 1

    b = mult(invert(sub(identity(len(q)), q)),r)[0]
    common = lcm([f.denominator for f in b])
    return [x.numerator * common/x.denominator for x in b] + [common]

print(solution(test))
