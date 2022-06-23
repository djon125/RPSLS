from player import Player
import random
class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    
    def choose_gesture(self):
        self.choice = random.choice(self.possible_action)
        print(f'the {self.name} chose {self.choice} ')

