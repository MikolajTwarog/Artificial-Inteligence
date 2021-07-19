#!/usr/bin/env python3

from board import Board

class Game:
    def __init__(self, board, player1, player2):
        self.players = []
        self.players.append(player1)
        self.players.append(player2)
        self.score = [0]*2
        self.board = Board()

    def play(self, num_of_games):
        end = False
        for _ in range(num_of_games):
            i = 1
            while not self.board.end:
                i = (i+1)%2
                self.board.make_move(self.players[i].make_move(self.board))
                # self.board.print_board()
            if not self.board.check_draw():
                print("player", i+1, "won!")
                self.score[i] += 1
            self.board = Board()
            self.players[0].clear()
            self.players[1].clear()
        print("player1:", self.score[0])
        print("player2:", self.score[1])
        return