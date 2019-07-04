def yell(string):
    
    """
    returns a string in upper case letters with an exclamation mark
    >>> yell('Hello')
    'HELLO!'
    >>> yell('oh no')
    'OH NO!'
    >>> yell(1)
    Traceback (most recent call last):
        ...
    AttributeError: 'int' object has no attribute 'upper'
    """
    return string.upper() + "!"

