import random
from palavras import palavras
import string

def buscar_palavra_valida(palavras):
    palavra = random.choice(palavras) # escolhe aleatoriamente uma palavra da lista
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)
    
    return palavra.upper()

def forca():
    palavra = buscar_palavra_valida(palavras)
    letras_palavra = set(palavra) # letras na palavra
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set() # as que o jogador tentou adivinhar
    vidas = 6

    # entrada do jogador
    while len(letras_palavra) > 0 and vidas > 0:
    
        # letras usadas
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Você possui', vidas,'vidas restantes e já usou estas letras: ', ' '.join(letras_usadas))

        # estado da palavra (ex. P A L _ V R A)
        lista_palavra = [letra if letra in letras_usadas else '_' for letra in palavra]
        print('Palavra atual: ', ' '.join(lista_palavra))

        tentativa = input('Tente uma letra: ').upper()
        if tentativa in alfabeto - letras_usadas:
            letras_usadas.add(tentativa)
            if tentativa in letras_palavra:
                letras_palavra.remove(tentativa)
            else:
                vidas = vidas - 1 # tira uma vida se errar
                print('A palavra não contém esta letra.')
        
        elif tentativa in letras_usadas:
            print('Você já escolheu essa letra. Por favor, tente outra.')
        
        else:
            print('Caractere inválido. Por favor, tente novamente.')
    
    # quando len(letras_palavra) == 0 ou quando vidas == 0
    if vidas == 0:
        print('Você morreu, desculpe. A palavra era', palavra)
    else:
        print('Parabéns, você acertou a palavra: ', palavra)

forca()