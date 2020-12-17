import random

def jogar():
    usuario = input("Escolha: 'r' para Pedra, 'p' para Papel e 's' para Tesoura\n")
    computador = random.choice(['r', 'p', 's'])

    if usuario == computador:
        return print('Empatou!')
    
    if venceu(usuario, computador):
        return print('Você ganhou!')

    return print('Você perdeu!')

def venceu(jogador, oponente):
    # r > s, s > p, p > r    
    # retorna verdadeiro se o jogador venceu
    if (jogador == 'r' and oponente == 's') or (jogador == 's' and oponente == 'p') or (jogador == 'p' and oponente == 'r'):
        return True

jogar()