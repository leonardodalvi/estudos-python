"""
Tic Tac Toe class + game play implementation by Kylie Ying
YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import math
import time
from jogador import JogadorHumano, JogadorComputadorAleatorio, JogadorComputadorInteligente


class TicTacToe():
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()
        self.ganhador_atual = None

    @staticmethod
    def criar_tabuleiro():
        return [' ' for _ in range(9)]

    def mostrar_tabuleiro(self):
        for row in [self.tabuleiro[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def mostrar_tabuleiro_nums():
        # 0 | 1 | 2
        number_tabuleiro = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_tabuleiro:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, quadrado, letra):
        if self.tabuleiro[quadrado] == ' ':
            self.tabuleiro[quadrado] = letra
            if self.ganhador(quadrado, letra):
                self.ganhador_atual = letra
            return True
        return False

    def ganhador(self, quadrado, letra):
        # check the row
        row_ind = math.floor(quadrado / 3)
        row = self.tabuleiro[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letra for s in row]):
            return True
        col_ind = quadrado % 3
        column = [self.tabuleiro[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letra for s in column]):
            return True
        if quadrado % 2 == 0:
            diagonal1 = [self.tabuleiro[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letra for s in diagonal1]):
                return True
            diagonal2 = [self.tabuleiro[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letra for s in diagonal2]):
                return True
        return False

    def quadrados_vazios(self):
        return ' ' in self.tabuleiro

    def num_quadrados_vazios(self):
        return self.tabuleiro.count(' ')

    def jogadas_disponiveis(self):
        return [i for i, x in enumerate(self.tabuleiro) if x == " "]


def play(game, jogador_x, jogador_o, print_game=True):

    if print_game:
        game.mostrar_tabuleiro_nums()

    letra = 'X'
    while game.quadrados_vazios():
        if letra == 'O':
            quadrado = jogador_o.jogada(game)
        else:
            quadrado = jogador_x.jogada(game)
        if game.make_move(quadrado, letra):

            if print_game:
                print(letra + ' fez uma jogada no quadrado {}'.format(quadrado))
                game.mostrar_tabuleiro()
                print('')

            if game.ganhador_atual:
                if print_game:
                    print(letra + ' venceu!')
                return letra  # ends the loop and exits the game
            letra = 'O' if letra == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    jogador_x = JogadorComputadorInteligente('X')
    jogador_o = JogadorHumano('O')
    t = TicTacToe()
    play(t, jogador_x, jogador_o, print_game=True)