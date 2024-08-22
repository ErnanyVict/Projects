nome = input("Digite seu nome: ")
tamanho_nome = len(nome)
c = 0
novo_nome = ''
while c < tamanho_nome:
    novo_nome += f'*{nome[c]}'
    c += 1
print(novo_nome)