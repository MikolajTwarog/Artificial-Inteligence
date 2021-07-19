#!/usr/bin/env python3

import numpy
import random

def draw():
    card = random.randint(1, 13)
    if card >= 10:
        return 10
    if card == 1:
        return 11
    return card

class Game:

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.dealer_card = 0
        self.dealer_points = 0
        self.dealer_ace = 0
        self.player_points = 0
        self.player_ace = 0
        self.games_count = 0
        self.ongoing = False


    def hit(self):
        if self.ongoing == False:
            raise ValueError('Game is not ongoing', self.player_points, self.dealer_points)
        card = draw()
        self.player_points += card
        if card == 11:
            self.player_ace += 1
        if self.player_points > 21 and self.player_ace:
            self.player_points -= 10
            self.player_ace -= 1
        if self.player_points > 21:
            self.losses += 1
            self.ongoing = False

    def dealer_hit(self):
        if self.ongoing == False:
            raise ValueError('Game is not ongoing', self.player_points, self.dealer_points)
        card = draw()
        self.dealer_points += card
        if card == 11:
            self.dealer_ace += 1
        if self.dealer_points > 21 and self.dealer_ace:
            self.dealer_points -= 10
            self.dealer_ace -= 1
        self.dealer_card = card
        if self.dealer_points > 21:
            self.wins += 1
            self.ongoing = False


    def start(self):
        self.games_count += 1
        self.dealer_card = 0
        self.dealer_points = 0
        self.dealer_ace = 0
        self.player_points = 0
        self.player_ace = 0
        self.ongoing = True
        self.dealer_hit()
        self.dealer_hit()
        self.hit()
        self.hit()
        if self.player_points == 21:
            if self.dealer_points < 21:
                self.wins += 1
            self.ongoing = False
            return
        while self.player_points < 12:
            self.hit()

    def stick(self):
        if self.ongoing == False:
            return
        while self.dealer_points < 17:
            self.dealer_hit()
        if self.ongoing == False:
            return
        if self.player_points > self.dealer_points:
            self.wins += 1
        if self.player_points < self.dealer_points:
            self.losses += 1
        self.ongoing = False


# game = Game()
# game.start()
# print(game.dealer_card)
# print(game.player_points)

# while(True):
#     decision = input()
#     if decision == "stick":
#         game.stick()
#         print("score:", game.score)
#     if decision == "hit":
#         game.hit()
#         print(game.player_points)
#     if game.ongoing == False:
#         break
