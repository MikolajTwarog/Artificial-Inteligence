#!/usr/bin/env python3

from blackjack import Game

game = Game()

for i in range(0, 5000000):
    game.start()
    while (True):
        if game.player_ace:
            if game.player_points <= 17:
                game.hit()
                continue
            if game.player_points == 18 and game.dealer_card >= 9:
                game.hit()
                continue
            break
        else:
            if game.player_points <= 16 and game.dealer_card >= 7:
                game.hit()
                continue
            if game.player_points <= 12 and game.dealer_card <= 3:
                game.hit()
                continue
            if game.player_points <= 11:
                game.hit()
                continue
            break
    game.stick()

print("wins:", game.wins/game.games_count)
print("losses:", game.losses/game.games_count)