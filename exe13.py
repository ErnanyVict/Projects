
def mult(*args):
    total, *args = args   
    for numero in args:
        total = total * numero
    return total
resultado = mult(1, 2, 3, 4, 10)
print(resultado)

def imparoupar(numero):
    if numero % 2 == 0:
        return f'{numero} é PAR'
    else:
        return f'{numero} é ÍMPAR'
print(imparoupar(3))
print(imparoupar(2))