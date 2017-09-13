from functools import reduce

def fact(n):
    fact_lamba = lambda x, y: x * y
    return reduce(fact_lamba, range(1,n+1))
