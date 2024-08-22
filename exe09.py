'''Calculadora com while'''

i  = 1
while i ==  1:
    try:
        numero1 = int(input("Escreva um número: "))
        numero2 = int(input("Escreva outro número: "))
        operador = int(input("Digite o operador (+ - * /): "))
   
    except:
        print("Digite dois números inteiros")
        continue
    if operador == '+':
        conta = numero1 + numero2
    elif operador == '-':
        conta = numero1 - numero2
    elif operador == '*':
        conta = numero1 * numero2
    elif operador == '/':
        conta = numero1 / numero2
    else:
        print("Digite um dos 4 operadores citados acima")
        continue
    print(f"{numero1} {operador} {numero2} = {conta}")
    break
            
