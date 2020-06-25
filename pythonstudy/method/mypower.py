def power(x):
    if  not isinstance(x ,(int,float)):
        raise  TypeError('Bad Operand Type') #raise TypeError('Bad Operand Type')
    return  x**2
print(power(1.2))
def power(x,n):
    if not isinstance(x, (int, float)) or not  isinstance(n, (int, float)):
        raise TypeError('Bad Operand Type')  # raise TypeError('Bad Operand Type')
    return x ** n
print(power(2,3))

def powerbywhile(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s