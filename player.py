class Player:
    def __init__(self, name):
        self.score = 0
        self.choice = None
        self.name = name
        self.possible_action = ["rock", "paper", "scissors", "lizard", "spock"]
