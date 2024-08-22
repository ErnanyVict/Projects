perguntas = [{
    'Pergunta': 'Quanto é 2 + 2?',
    'Opções': ['1', '3', '4', '5'],
    'Resposta': '4'},
    {
    'Pergunta': 'Quanto é 5 * 5?',
    'Opções': ['25', '55', '10', '51'],
    'Resposta': '25'},
    {
    'Pergunta': 'Quanto é 10 / 2?',
    'Opções': ['4', '5', '2', '1'],
    'Resposta': '5'   
    }
]
acertos = 0
for pergunta in perguntas:
        print(pergunta['Pergunta'])
        
        print('\nOpções:')
        for indice in range(0, 4):
            print(f'{indice})', pergunta['Opções'][indice])
        try:
            resposta_dada = int(input('Escolha uma opção: '))

            if  pergunta['Opções'][resposta_dada] == pergunta['Resposta']:
                print('ACERTOU!!!\n')
                acertos += 1
            else:
                print('Errou!!!\n')
        except:
            print('Errou!!!\n')     
print(f'Você acertou {acertos}/3') 