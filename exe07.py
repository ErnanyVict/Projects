nome = input("Digite seu primeiro nome: ")
qtd_nome = len(nome)
if qtd_nome <= 4:
    print("Seu nome é curto")
elif qtd_nome > 4 and qtd_nome <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")