import random

def adivinhar(x):
    numero_aleatorio = random.randint(1, x)
    tentativa = 0
    while tentativa != numero_aleatorio:
        tentativa = int(input(f'Tente adivinhar um número que está entre 1 e {x}: '))
        if tentativa < numero_aleatorio:
            print('Desculpe, tente novamente. Muito baixo.')
        elif tentativa > numero_aleatorio:
            print('Desculpe, tente novamente. Muito alto.')
    print(f'Uhul! Parabéns! Você acertou o número {numero_aleatorio}!')

def computador_adivinhar(x):
    input('Pense em um número de 1 a 1000! Assim que estiver pronto, pressione enter. ')
    baixo = 1
    alto = x
    feedback = ''
    while feedback != 'c':
        if baixo != alto:
            tentativa = random.randint(baixo, alto)
        else:
            tentativa =  baixo # também poderia ser alto, já que baixo = alto
        feedback = (input(f'{tentativa} é muito alto (A), muito baixo (B) ou está correto (C)?? ').lower())
        if feedback == 'a':
            alto = tentativa - 1
        elif feedback == 'b':
            baixo = tentativa + 1
    print(f'Uhul! O computador adivinhou seu número, {tentativa}, corretamente!')

jogar = input('Gostaria de adivinhar um número gerado pelo computador (1) ou de faze-lo adivinhar um número que você está pensando (2)? ')

if jogar == '1':

    adivinhar(1000)

elif jogar == '2':

    computador_adivinhar(1000)

else:
    print('Vocë precisa indicar qual modalidade gostaria de jogar (1 ou 2).')