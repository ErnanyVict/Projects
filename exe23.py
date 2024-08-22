# Unir duas listas

from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    uniao = []
    menor = range(min(len(lista1), len(lista2)))
    for n in menor:
        uniao.append((cidades[n], estados[n]))
    return uniao

print(zipper(cidades, estados))
print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados)))