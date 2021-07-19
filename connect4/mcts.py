import math
import random
import numpy as np
from collections import defaultdict
from board import Board

class PlayerMCTS:
    class Node:
        def __init__(self, state, wins, parent, move):
            self.state = state
            self.wins = wins
            self.visits = 0
            self.parent = parent
            self.move = move
            self.children = []

        def ucb1(self):
            if self.visits == 0:
                return math.inf
            return (self.wins/self.visits) + 2*math.sqrt(2*math.log(self.parent.visits)/self.visits)

    def __init__(self, num_of_games, is_first_player):
        self.is_first_player = is_first_player
        self.num_of_games = num_of_games

    def selection(self, node):
        while len(node.children) != 0:
            children = [child.ucb1() for child in node.children]
            node = node.children[np.argmax(children)]
        return node

    def expansion(self, node):
        children = node.state.get_children()
        node.children = [self.Node(child, 0, node, move) for child, move in children]

    def simulation(self, node):
        state = Board()
        state.board = [list(x) for x in node.state.board]
        state.moves = node.state.moves
        while not state.end and len(state.get_possible_moves()) > 0:
            if len(state.get_possible_moves()) == 0:
                print("dupa")
                print(state.check_draw())
                print(state.end)
                print(state.check_if_end(0, 0, 1))
                state.print_board()
            state.make_move(random.choice(state.get_possible_moves()))
        if state.check_draw():
            return 0
        # print((state.moves)%2 == self.is_first_player)
        return (state.moves)%2 == self.is_first_player

    def backpropagation(self, node, result):
        while node is not None:
            node.visits += 1
            if node.state.moves%2 == self.is_first_player:
                node.wins += result
            node = node.parent

    def train(self, node):
        for _ in range(0, self.num_of_games):
            new_node = self.selection(node)
            self.expansion(new_node)
            result = self.simulation(new_node)
            # print(result)
            self.backpropagation(new_node, result)

    def make_move(self, board):
        state = Board()
        state.board = [list(x) for x in board.board]
        state.moves = board.moves
        node = self.Node(state, 0, None, 0)
        self.train(node)
        moves = [child.visits for child in node.children]
        # print([child.wins for child in node.children])
        return node.children[np.argmax(moves)].move

    def clear(self):
        pass
        # self.map = dict()