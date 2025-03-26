""" 
Pol Alaminos Martorell 
POL ALAMINOS MARTORELL
>>> esPrimo(4)
False

>>> esPrimo(-2)
True

>>> esPrimo(-4)
False

"""


import math


def esPrimo(num):
    """
    Devuelve True si su argumento es primo y False si no lo es
    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
    >>> esPrimo(1023)
    False
    
    >>> esPrimo(1021)
    True
    
    """
    
    for it in range(2, num):
        if num % it == 0: 
            return False      
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()