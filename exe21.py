from copy import deepcopy

produtos = [{'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90},]

produtos_ordenados_por_nome = deepcopy(produtos)
produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key=lambda item: item['nome'])

a = deepcopy(produtos)
produtos_ordenados_por_preco = []

for p in a:
    produto_s = {chave: valor + (valor/10) if isinstance(valor, float) 
    else valor for chave, valor in p.items()}
    produtos_ordenados_por_preco.append(produto_s)


produtos_ordenados_por_preco = sorted(produtos_ordenados_por_preco, key=lambda item: item['preco'])


print("Produtos originais: \n")
for original in produtos:
    print(original)
print('\n')

print("Produtos ordenados pelo nome: \n")
for p in produtos_ordenados_por_nome:
    print(original)
print('\n')

print("Produtos ordenados por preço: \n")
for ws in produtos_ordenados_por_preco:
    print(ws)
print('\n')