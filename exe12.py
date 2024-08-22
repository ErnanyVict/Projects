import re
import random

while True:
    soma1 = 0
    soma2 = 0
    digitos = ''
    cpf_digitado = ''
    try:
        for i in range(9):
            cpf_digitado += str(random.randint(0, 9))
        ''' cpf_digitado = input("Digite seu cpf: ")
        cpf_digitado = re.sub(r'[^0-9]', '', cpf_digitado)'''
    except:
        
        print("cpf digitado errado! Por favor digite apenas os digitos do seu cpf")
        continue
    confirmacao = cpf_digitado[9:]
    cpf_usado = cpf_digitado[: 9]
    # soma do primeiro dígito
    for i in range (2, 11): 
        soma1 += (-i + 12) * int(cpf_usado[i-2])
    soma1 = soma1 % 11
    if soma1 < 2:
        digitos = '0'
    else:
        digitos = str(11 - soma1)
    cpf_usado += digitos

    # soma do segundo dígito
    for i in range(2, 12):
        soma2 += (13 - i) * int(cpf_usado[i - 2])
    soma2 = soma2 % 11 
    if soma2 < 2:
        digitos += '0'
    else:
        digitos += str(11 - soma2)

    if digitos == confirmacao:
        print(f"{cpf_digitado} é VÁLIDO")
    else:
        print(f'{cpf_digitado} é INVÁLIDO') 