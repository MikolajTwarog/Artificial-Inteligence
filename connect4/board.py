#!/usr/bin/env python3


class Board:

    def __init__(self):
        self.board = [[0]*7 for i in range(6)]
        self.moves = 0
        self.end = False

    def check_vertical(self, row, column, who):
        line = 0
        for i in range(row, 6):
            if self.board[i][column] == who:
                line += 1
            else:
                break
        return line

    def check_horizontal(self, row, column, who):
        line = 0
        for i in range(column, 7):
            if self.board[row][i] == who:
                line += 1
            else:
                break
        for i in range(column-1, -1, -1):
            if self.board[row][i] == who:
                line += 1
            else:
                break
        return line

    def check_diagonal(self, row, column, who):
        line = 1
        for i in range(1, min(7 - column, 6 - row)):
            if self.board[row+i][column+i] == who:
                line += 1
            else:
                break
        for i in range(1, min(column + 1, row + 1)):
            if self.board[row-i][column-i] == who:
                line += 1
            else:
                break

        line2 = 1
        for i in range(1, min(column + 1, 6 - row)):
            if self.board[row+i][column-i] == who:
                line2 += 1
            else:
                break
        for i in range(1, min(7 - column, row + 1)):
            if self.board[row-i][column+i] == who:
                line2 += 1
            else:
                break

        return max(line, line2) 

    def check_draw(self):
        for i in range(0, 7):
            if self.board[0][i] == 0:
                return False
        return True

    def check_if_end(self, row, column, who):
        line = max(self.check_vertical(row, column, who), 
            self.check_horizontal(row, column, who), 
            self.check_diagonal(row, column, who))
        return line >= 4 or self.check_draw()

    def make_move(self, column):
        if self.board[0][column] != 0:
            return False
        who = (self.moves % 2) + 1
        row = 5
        while self.board[row][column] != 0:
            row -= 1
        self.board[row][column] = who
        self.end = self.check_if_end(row, column, who)
        self.moves += 1
        return True

    def get_children(self):
        who = (self.moves % 2) + 1
        children = []
        for i in range(0, 7):
            child = Board()
            child.moves = self.moves
            child.board = [list(x) for x in self.board]
            if child.make_move(i):
                children.append((child, i))
        return children

    def get_possible_moves(self):
        moves = []
        for i in range(0, 7):
            if self.board[0][i] == 0:
                moves.append(i)
        return moves
    
    def print_board(self):
        for i in self.board:
            b = ""
            for j in i:
                if j == 0:
                    b += '.'
                elif j == 1:
                    b += 'O'
                else:
                    b += 'X'
                b += " "
            print(b)
        print("0 1 2 3 4 5 6")
        print()
        return
