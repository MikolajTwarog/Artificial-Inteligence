import math
import random

def pp(x):
    if x == 3:
        return 10000
    return 10**x

class PlayerMinimax:
    def __init__(self, depth, is_player_one):
        self.depth = depth
        self.is_player_one = is_player_one
        self.states = dict()

    def heuristic(self, board):
        heur = 0
        state = board.board
        for column in range(0, 7):
            for row in range(0, 6):
                line = 0
                for i in range(row, 6):
                    if state[i][column] == 1:
                        line += 1
                    else:
                        break
                heur += pp(line)
                line = 0
                for i in range(row, 6):
                    if state[i][column] == 2:
                        line += 1
                    else:
                        break
                heur -= pp(line)

                line = 0
                for i in range(column, 7):
                    if state[row][i] == 1:
                        line += 1
                    else:
                        break
                heur += pp(line)
                line = 0
                for i in range(column, 7):
                    if state[row][i] == 2:
                        line += 1
                    else:
                        break
                heur -= pp(line)

                line = 0
                for i in range(0, min(7 - column, 6 - row)):
                    if state[row+i][column+i] == 1:
                        line += 1
                    else:
                        break
                heur += pp(line)
                line = 0
                for i in range(0, min(7 - column, 6 - row)):
                    if state[row+i][column+i] == 2:
                        line += 1
                    else:
                        break
                heur -= pp(line)

                line = 0
                for i in range(0, min(column + 1, 6 - row)):
                    if state[row+i][column-i] == 1:
                        line += 1
                    else:
                        break
                heur += 10**line
                line = 0
                for i in range(0, min(column + 1, 6 - row)):
                    if state[row+i][column-i] == 2:
                        line += 1
                    else:
                        break
                heur -= 10**line
        return heur

    def make_move(self, board):
        best = self.minimax(board, self.is_player_one, self.depth, -math.inf, math.inf)[1]
        # print(best)
        return best

    def heur2(self, child):
        return self.heuristic(child[0])

    def minimax(self, board, is_player_one, depth, alpha, beta):
        if (str(board.board), depth) in self.states:
            # print(self.states[(board.board, depth)])
            return self.states[(str(board.board), depth)]
        best_score = -math.inf if is_player_one else math.inf

        if board.end:
            # board.print_board()
            return best_score, -1
        if depth == 0:
            # print(self.heuristic(board))
            # board.print_board()
            return self.heuristic(board), -1

        best_move = -1
        children = board.get_children()
        children.sort(key = self.heur2, reverse = is_player_one)
        for i in children:
            child, move = i
            score = self.minimax(child, not is_player_one, depth-1, alpha, beta)[0]
            if (is_player_one and score > best_score) or (not is_player_one and score < best_score):
                best_score = score
                best_move = move
            if is_player_one:
                alpha = max(alpha, score)
            else:
                beta = min(beta, score)
            if alpha >= beta:
                break
        if best_move == -1:
            best_move = random.choice(board.get_possible_moves())
        
        self.states[(str(board.board), depth)] = (best_score, best_move)
        return best_score, best_move

    def clear(self):
        self.states = dict()
        
        

