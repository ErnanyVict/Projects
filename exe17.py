# Escrever até a letra determinada com base no número digitado pelo user

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 
            'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

while True:
    
    try:
        numero_digitado = int(input("Digite até qual posição do alfabeto será digitada: "))
    except:
        print("ERRO. Digite um número inteiro")
        continue
    
    numero = 1
        
    alfabeto_iter = iter(alfabeto)
    
    try:
        while numero <= numero_digitado:
            print(f'{next(alfabeto_iter)}', end=', ')
            numero += 1
        break
    
    except:
        print("\nERRO. Digite um numero até 26")
        continue