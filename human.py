from player import Player
class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.choice = input('Chose: 1 for rock, 2 for paper, 3 for scissors, 4 for lizard 5 for spock ')
        if self.choice == '1':
            self.choice = 'rock'
            print(f'{self.name} chooses {self.choice}')
        elif self.choice == '2':
            self.choice = 'paper'
            print(f'{self.name} chooses {self.choice}')
        elif self.choice == '3':
            self.choice = 'scissors'
            print(f'{self.name} chooses {self.choice}')
        elif self.choice == '4':
            self.choice = 'lizard'
            print(f'{self.name} chooses {self.choice}')
        elif self.choice == '5':
            self.choice = 'spock'
            print(f'{self.name} chooses {self.choice}')
        else:
            print('Not A Valid Input, Try Again:')
            self.choose_gesture()

            



