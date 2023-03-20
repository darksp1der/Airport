
"""
The function used to get the first element of the solution
(the first passenger/plane)
"""


def init(start):
    return start


'''
The function used to get the next possible solution
(the next passenger/plane)
'''


def get_next(sol,pos):
    return sol[pos] + 1


'''
The function in which we check the properties
from the cond function
'''


def is_consistent(sol,start):
    iscons = True
    i = 0
    while i<len(sol)-1 and iscons==True:
        if sol[i]==sol[len(sol)-1] or cond(sol[i],sol[len(sol)-1],start) is False:
            iscons = False
        else:
            i = i + 1
    return iscons


'''
The function in which we check for the length of the current 
possible solution
'''


def is_solution(solution,n,start):
    return len(solution) == n


'''
The function in which we keep each solution
'''


def back_rec(n,solution,start):
    initvalue = init(start)
    solution.append(initvalue)
    elem = get_next(solution, len(solution) - 1)
    while elem <= n:
        solution[len(solution)-1] = elem
        if is_consistent(solution,start) is True:
            if is_solution(solution,n,start) is True:
                yield solution
            else:
                yield from back_rec(n,solution[:],start)
        elem = get_next(solution,len(solution)-1)


'''
 10)Form groups of 𝒌 passengers from the same plane but with different last names
 11)Form  groups  of  𝒌 planes  with  the  same  destination  but  belonging  to  different  airline companies
 k is given by the user
 For exercise 10, start is 1 and for exercise 11, start is 2
'''


def cond(a,b,start):
    if start == 1:
        if a.get_lastname() == b.get_lastname():
            return False
        return True
    else:
        if a.get_destination() == b.get_destination() and a.get_airline() != b.get_airline():
            return True
        return False

