#!/usr/bin/env python3

import random
import numpy as np
from collections import defaultdict
from blackjack import Game


def make_move(Q, game):
    if game.ongoing == False:
        return (0, 0, 0)
    action = 0
    state = (game.player_points, game.player_ace, game.dealer_card)
    if decision(Q[state]) == 0:
        game.stick()
        actions = 0
    else:
        game.hit()
        action = 1
    state = (game.player_points, game.player_ace, game.dealer_card)
    reward = game.wins-game.losses
    return (state, action, reward)


visited = defaultdict(lambda: np.zeros(2))
returns_sum = defaultdict(lambda: np.zeros(2))
Q = defaultdict(lambda: [0, 0])

epsilon = 0.1
alfa = 0.02
gamma = 0.2

def decision(a):
    better = np.argmax(a)
    chance = [0, 0]
    chance[better] = 1 - epsilon/2
    chance[1-better] = epsilon/2
    return np.random.choice(2, 1, chance)

for k in range(0, 500000):
    game = Game()
    game.start()
    state = (game.player_points, game.player_ace, game.dealer_card)
    # action = np.random.choice(2, 1, Q[state])
    action = decision(Q[state])
    while game.ongoing:
        s_prime, action, reward = make_move(Q, game)
        a_prime = 0
        if decision(Q[s_prime]):
            a_prime = 0
        else:
            a_prime = 1
        Q[state][action] += alfa*(reward + gamma*Q[s_prime][a_prime] - Q[state][action])
        state = s_prime




for i in [True, False]:
    for j in range(12, 22):
        for k in range(2, 12):
            print(j, i, k, ":", np.argmax(Q[(j, i, k)]))

game = Game()

for i in range(0, 500000):
    game.start()
    while (True):
        if game.ongoing == False:
            break
        state = (game.player_points, game.player_ace, game.dealer_card)
        if np.argmax(Q[state]) == 0:
            game.stick()
        else:
            game.hit()

print("wins:", 100*game.wins/game.games_count, '%')
print("losses:", 100*game.losses/game.games_count, '%')
