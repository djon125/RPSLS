from player import Player
class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        user_input = input(f'Chose: 1 for {self.possible_action[0]}, 2 for {self.possible_action[1]}, 3 for {self.possible_action[2]}, 4 for {self.possible_action[3]} 5 for {self.possible_action[4]}: ')
        if user_input == '1':
            self.choice = self.possible_action[0]
            print(f'{self.name} chooses {self.choice}')
        elif user_input == '2':
            self.choice = self.possible_action[1]
            print(f'{self.name} chooses {self.choice}')
        elif user_input == '3':
            self.choice = self.possible_action[2]
            print(f'{self.name} chooses {self.choice}')
        elif user_input == '4':
            self.choice = self.possible_action[3]
            print(f'{self.name} chooses {self.choice}')
        elif user_input == '5':
            self.choice = self.possible_action[4]
            print(f'{self.name} chooses {self.choice}')
        else:
            print('Not A Valid Input, Try Again:')
            self.choose_gesture()

            

#child class of player

