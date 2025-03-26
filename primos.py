""" 
Pol Alaminos Martorell 

"""


import math


def esPrimo(num):
    """
    Devuelve True si su argumento es primo y False si no lo es
    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
    """
    
    for it in range(2, num):
        if num % it == 0: 
            return False      
    return True

def primos(lim):
    """
    Devuelve una lista con los números primos menores que el argumento
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """

    return tuple(i for i in range(2, lim) if esPrimo(i))

def descompon(num):
    """
    Devuelve una tupla con la descomposición en números primos del argumento ordenada de menor a mayor.
    En este caso utilizamos la Propiedad de los números primos donde:
    si un número compuesto n tiene un divisor d, d <= sqrt(n)
    
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """

    desc = []
    divisor = 2
    while divisor **2 <= num:     #Si d**2 > n ya no existen más divisores por lo tanto termina el bucle.
        if num % divisor == 0:    #Si la división es exacta forma parte de la descomposición.
            desc.append(divisor)
            num //= divisor       #Dividimos el número por el divisor como en la descomposición.
        else:
            divisor += 1          #Si la division no es exacta aumentamos divisor hasta sqrt(num) como máximo.
    if num > 1:
        desc.append(num)      #Si el último valor de num es mayor que 1, significa que es un primo divisor.
    return tuple(desc) 
    
def mcm(num1, num2):
    """
    Devuelve el mínimo común múltiplo de los dos argumentos
    >>> mcm(90, 14)
    630
    """
    desc1 = descompon(num1)
    desc2 = descompon(num2)
    mcmList = list(desc1)                       #Añadimos todos los múltimplos del num1 a la lista.
    for i in range(len(desc2)):                 #Recorremos los múltiplos del num2.
        quantDesc1 = mcmList.count(desc2[i])
        quantDesc2 = desc2.count(desc2[i])
        if quantDesc1 < quantDesc2:             #Comprueba si los múltiplos están ya en la lista y si lo estan, nos aseguramos
            n = quantDesc2 - quantDesc1         #que coja la máxima cantidad de múltiplos.
            for j in range(n):
                mcmList.append(desc2[i])
    return math.prod(mcmList)                   #Devuelve el producto de todos los múltiplos (mcm).

def mcd(num1, num2):
    """
    Devuelve el máximo común divisor de los dos argumentos
    >>> mcd(924, 780)
    12
    """
    desc1 = descompon(num1)
    desc2 = descompon(num2)
    list2 = list(desc2)
    mcdList = []
    for i in range(len(desc1)):
        if desc1[i] in list2:
            mcdList.append(desc1[i])
            list2.remove(desc1[i])
    return math.prod(mcdList)                    #Devuelve el producto de todos los múltiplos (mcd).

def mcmN(*nums):
    """Devuelve el mínimo común múltiplo de todos los argumentos
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    
    MCM = 1
    for i in range(len(nums)):
        MCM = mcm(MCM, nums[i])
    return MCM

def mcdN(*nums):
    """
    Devuelve el máximo común divisor de todos los argumentos
    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    
    MCD = nums[0]
    for num in nums[1: ]:
        MCD = mcd(MCD, num)
    return MCD

if __name__ == "__main__":
    import doctest
    doctest.testmod()