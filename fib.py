'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    # TODO = fill in the code here, and return the correct result using the return keyword
    
    # for fib number 0 to 2 we have to do it manually
    if n <= 0:
        return []
    elif n == 1:
        return [1]    
    elif n == 2:
        return [1, 1]
        
    fib = [1, 1]
    
    for i in range(n-2): # -2 means we ignore the first 2 sequence
        fib.append(fib[-1] + fib[-2]) # added the last two number from the last
    return fib        
    
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
