from player import Player
class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.choice = input('pick ')
        print(f'{self.name} chose {self.choice}')
        if self.choice == '1':
            self.choice = 'rock'
        elif self.choice == '2':
            self.choice = 'paper'
        elif self.choice == '3':
            self.choice = 'scissors'
        elif self.choice == '4':
            self.choice = 'lizard'
        elif self.choice == '5':
            self.choice = 'spock'
        else:
            print('Not A Valid Input, Try Again:')
            self.choose_gesture()

            



