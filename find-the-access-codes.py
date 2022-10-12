# Fortunately, now that you're Commander Lambda's personal assistant, Lambda has confided to you that all the access codes are "lucky triples" in order to make it easier to find them in the lists. A "lucky triple" is a tuple (i, j, k) where i divides j and j divides k, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

# Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The solution fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0. 

# For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the solution 3 total.


# def solution(l): #runtime ??
#     length = len(l)
#     lucky_triple = 0
#     for i in range(length-2):
#         for j in range(i+1, length-1):
#             if l[j]%l[i] == 0: # check if the rest is float
#                 for k in range(j+1, length):
#                     if l[k]%l[j] == 0: # check if the rest is float
#                         lucky_triple+= 1
#     return lucky_triple

def solution(l):
    lucky_triple = 0
    allMatchs = []

    for i, element in enumerate(l):
        match = []
        for el in l[i+1:]:
            if el%element == 0: # check if the rest is float
                match.append(el)
        allMatchs.append(match)
    
    for p, l_match in allMatchs:
        l[p] = 0
        temp = l[:]
        for x in l_match:
            p_geral = temp.index(x)
            lucky_triple += len(allMatchs[p_geral])
            temp[p_geral] = 0

    return lucky_triple