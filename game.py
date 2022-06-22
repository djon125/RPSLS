from ai import Ai


class Game:
    def __init__(self):
        self.player_one = Ai('robo_one')

    def run_game(self):
        self.player_one.choose_gesture()


