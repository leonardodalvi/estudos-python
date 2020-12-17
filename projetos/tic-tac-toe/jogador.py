"""
Tic-Tac-Toe players using inheritance implementation by Kylie YIng
YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import math
import random


class Jogador():
    def __init__(self, letra):
        self.letra = letra

    def jogada(self, jogo):
        pass


class JogadorHumano(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def jogada(self, jogo):
        quadrado_valido = False
        val = None
        while not quadrado_valido:
            square = input('Vez de ' + self.letra + '. Faça sua jogada (0-9): ')
            try:
                val = int(square)
                if val not in jogo.jogadas_disponiveis():
                    raise ValueError
                quadrado_valido = True
            except ValueError:
                print('Quadrado inválido. Tente novamente.')
        return val


class JogadorComputadorAleatorio(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def jogada(self, jogo):
        square = random.choice(jogo.jogadas_disponiveis())
        return square


class JogadorComputadorInteligente(Jogador):
    def __init__(self, letter):
        super().__init__(letter)

    def jogada(self, jogo):
        if len(jogo.jogadas_disponiveis()) == 9:
            square = random.choice(jogo.jogadas_disponiveis())
        else:
            square = self.minimax(jogo, self.letra)['position']
        return square

    def minimax(self, estado, jogador):
        max_player = self.letra  # yourself
        outro_jogador = 'O' if jogador == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if estado.ganhador_atual == outro_jogador:
            return {'position': None, 'score': 1 * (estado.num_quadrados_vazios() + 1) if outro_jogador == max_player else -1 * (
                        estado.num_quadrados_vazios() + 1)}
        elif not estado.quadrados_vazios():
            return {'position': None, 'score': 0}

        if jogador == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in estado.jogadas_disponiveis():
            estado.make_move(possible_move, jogador)
            sim_score = self.minimax(estado, outro_jogador)  # simulate a game after making that move

            # undo move
            estado.tabuleiro[possible_move] = ' '
            estado.ganhador_atual = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if jogador == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best