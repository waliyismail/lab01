'''
make a command line calculator

DIFFICULTY = MEDIUM
TOPICS = strings, variables, lists

your task is to write a command line calculator
this task is easy since we can use the eval function to do most of the legwork
however, we need to parse possible invalid user input. This is your task

return None if invalid input. Otherwise return the result
'''

def calculate(s):
    '''
    >>> calculate("1+3")
    4
    >>> calculate("1+3*4/3")
    5.0
    >>> calculate("(1+3)*5")
    20
    >>> calculate("-----1")
    -1
    >>> calculate("-+-1")
    1
    >>> calculate(\'print("bad guy coming to hack")\')
    '''
    # TODO = fill in this function
    
    
    operator = "+-/*" #list of operator
    for ch in s:
        if ch.isalpha():
            return None
    for i in range(len(operator)): # to get the index of operator list
    
        if operator[i] in s: #if the operator is in command line , we just eval
            return eval(s)

    return None
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
