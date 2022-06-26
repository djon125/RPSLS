from player import Player
import random
import time
class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    
    def choose_gesture(self):
        self.choice = random.choice(self.possible_action)
        time.sleep(1)
        print(f'{self.name} chooses {self.choice} ')


#child class oif player