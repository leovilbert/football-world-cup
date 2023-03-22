from random import choice

edicoes = [1930,1934,1938,1950,1954,1958,1962,1966,1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014,2018,2022]

vitorias = {'uruguai':[1930,1950], 'itália':[1934,1938,1982,2006], 'alemanha': [1954,1974,1990,2014], 'brasil': [1958,1962,1970,1994,2002], 'inglaterra': [1966], 'argentina': [1978,1986,2022], 'frança': [1998,2018], 'espanha': [2010]}

acertos = 0 

while True:
    if not edicoes:
        print('Parabéns, você sabe todos os campeões da Copa do Mundo!\n\n')
        break
    else:
        edicao = choice(edicoes)
        del edicoes[edicoes.index(edicao)]

    vencedores = ['uruguai','itália', 'alemanha', 'brasil', 'inglaterra', 'argentina', 'frança', 'espanha']

    resposta = input(f'Quem foi o campeão da Copa do Mundo em {edicao}? ').lower()

    if resposta not in vencedores:
        print('\nEsse país nunca venceu uma Copa do Mundo. Tente de novo!\n')

    elif edicao in vitorias.get(resposta):
        acertos += 1
        print('\nVocê acertou!')
        print(f'Total de acertos: {acertos}\n')

    else:
        print('\nVocê errou!')
        print(f'Total de acertos: {acertos}\n')
        break
