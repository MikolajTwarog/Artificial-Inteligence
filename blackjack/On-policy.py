#!/usr/bin/env python3

import random
import numpy as np
from collections import defaultdict
from blackjack import Game


def generate_episode(pi):
    game = Game()
    game.start()
    game.player_points = random.randint(12, 21)
    game.player_ace = random.randint(0, 1)
    states = []
    actions = []
    rewards = []
    while True:
        if game.ongoing == False:
            break
        state = (game.player_points, game.player_ace, game.dealer_card)
        states.append(state)
        if np.random.choice(2, 1, pi[state]) == 0:
            game.stick()
            actions.append(0)
        else:
            game.hit()
            actions.append(1)
        rewards.append(game.wins-game.losses)
    return (states, actions, rewards)


visited = defaultdict(lambda: np.zeros(2))
returns_sum = defaultdict(lambda: np.zeros(2))
Q = defaultdict(lambda: np.zeros(2))
policy = defaultdict(lambda: [0.5, 0.5])

gamma = 0.2
epsilon = 0.2

for k in range(0, 50000):
    states, actions, rewards = generate_episode(policy)
    G = 0
    for i, state in enumerate(reversed(states)):
        G = G*gamma + rewards[i]
        if (state, actions[i]) not in list(zip(states, actions))[:i]:
            visited[state][actions[i]] += 1.0
            returns_sum[state][actions[i]] += G
            Q[state][actions[i]] = returns_sum[state][actions[i]]/visited[state][actions[i]]
            action = np.argmax(Q[state])
            policy[state][action] = 1 - epsilon/2
            policy[state][1-action] = epsilon/2


for i in [True, False]:
    for j in range(12, 22):
        for k in range(2, 12):
            print(j, i, k, ":", np.argmax(policy[(j, i, k)]))

game = Game()

for i in range(0, 500000):
    game.start()
    while (True):
        if game.ongoing == False:
            break
        state = (game.player_points, game.player_ace, game.dealer_card)
        # if np.random.choice(2, 1, policy[state]) == 0:
        if np.argmax(policy[state]) == 0:
           game.stick()
        else:
            game.hit()

print("wins:", 100*game.wins/game.games_count, '%')
print("losses:", 100*game.losses/game.games_count, '%')
