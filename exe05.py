try:
    numero_str = input("Número inteiro: ")
    numero_inteiro = int(numero_str)
    condicao = numero_inteiro % 2
    if condicao == 0:
        print(f"{numero_inteiro} é PAR")
    else:
        print(f"{numero_inteiro} é ÍMPAR")
except:
    print("O número digitado não é inteiro")