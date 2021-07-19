#!/usr/bin/env python3

from board import Board
from player import Player
from game import Game
from minimaxAlphaBeta import PlayerMinimax
from mcts import PlayerMCTS

player1 = PlayerMinimax(7, True)
# player1 = Player()
# player1 = PlayerMCTS(100, True)
# player2 = PlayerMinimax(5, False)
# player2 = Player()
player2 = PlayerMCTS(10000, False)
board = Board()
game = Game(board, player1, player2)
game.play(10)