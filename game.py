from computer import Computer
from human import Human


class Game:
    def __init__(self):
        self.player_one = Computer('robo_one')
        self.player_two = Computer('robo_two')
        self.player_h = Human('human_one')

        
    def get_rules(self):
        print()
        print('Welcome to Rock Paper Scissor Lizard Spock')
        print('Each match will be besr of three')
        print('The rules are simple...')
        print(' Rock crushes Scissors\n Rock crushes Lizard\n Paper disproves Spock\n Paper covers Rock')
        print(' Scissors cuts Paper\n Scissors decapitates Lizard\n Lizard poisons Spock\n Lizard eats Paper')
        print(' Spock smashes Scissors\n Spock vaporizes Rock')



    def run_game(self):
        self.get_rules()
        self.player_h.choose_gesture()
        print(self.player_h.choice)
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        


        # while self.player_one.score or self.player_two.score < 3:
        #     if self.player_one.choice == self.player_two.choice:
        #         print('Tie')
        #     elif self.player_one.choice == 'rock' and self.player_two.choice == 'scissors':
        #         print('rock crushes scissors')
        #         self.player_one.score += 1
        #     elif self.player_one.choice == 'rock' and self.player_two.choie == 'lizard':
        #         print('rock crushes lizard')
        #         self.player_one += 1
        #     elif self.player_one.choice == 'paper' and self.player_two.choice == 'spock':
        #         print('paper disproves spock')
        #         self.player_one += 1
        #     elif self.player_one.choice == 'paper' and s





