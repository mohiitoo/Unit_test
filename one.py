
def Sum(x,y):
    return x + y


def Subtraction(x,y):
    return x - y


def Multiplication(x,y):
    return x * y

def Division(x,y):
    if y == 0:
        assert ZeroDivisionError('cant division number b zero')
    return x / y

