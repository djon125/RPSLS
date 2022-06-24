from operator import truediv
from computer import Computer
from human import Human
# import #time

class Game:
    def __init__(self):
        self.player_one = Computer('robo_one')
        self.player_two = Computer('robo_two')
        self.player_h = Human('human_one')
        self.player_h_two = Human('human_two')

        
    def get_rules(self):
        print()
        print('Welcome to Rock Paper Scissor Lizard Spock')
        print('Each match will be best of three')
        print('The rules are simple...')
        print(' Rock crushes Scissors\n Rock crushes Lizard\n Paper disproves Spock\n Paper covers Rock')
        print(' Scissors cuts Paper\n Scissors decapitates Lizard\n Lizard poisons Spock\n Lizard eats Paper')
        print(' Spock smashes Scissors\n Spock vaporizes Rock')



    def run_game(self):
        #self.get_rules()
        self.mode_select()
        pass
    
    
    def mode_select(self):
        game = True
        game_choice = input('Press 1 for human v computer 2 for human v human 3 for a suprise ')
        while game == True:
            if game_choice == '1':
                self.player_v_computer()
            elif game_choice == '2':
                self.player_v_player()
            elif game_choice == '3':
                self.computer_v_computer()
            else:
                print('That is not a vaild option, try again.')
                game_choice = input('Press 1 for human v computer 2 for human v human 3 for a suprise ')

        
    def computer_v_computer(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        while (self.player_one.score < 2) and (self.player_two.score < 2):
            if self.player_one.choice == self.player_two.choice:
                print('tie')
                print(f'{self.player_one.name} score is {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is {self.player_two.score}')
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
            elif self.player_one.choice == 'rock' and (self.player_two.choice == 'scissors' or self.player_two.choice == 'lizard'):
                self.player_one.score += 1
                print(f'{self.player_one.name} score is {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is {self.player_two.score}')
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
            elif self.player_one.choice == 'paper' and (self.player_two.choice == 'spock' or self.player_two.choice == 'rock'):
                self.player_one.score += 1
                print(f'robo_one score is {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is {self.player_two.score}')
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
            elif self.player_one.choice == 'scissors' and (self.player_two.choice == 'paper' or self.player_two.choice == 'lizard'):
                self.player_one.score += 1  
                print(f'{self.player_one.name} score is {self.player_one.score}')
                #time.sleep(1)
                print(f'{self.player_two.name} score is {self.player_two.score}')                       
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()  
            elif self.player_one.choice == 'lizard' and (self.player_two.choice == 'spock' or self.player_two.choice == 'paper'):
                self.player_one.score += 1
                print(f'{self.player_one.name} score is {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is {self.player_two.score}')
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
            elif self.player_one.choice == 'spock' and (self.player_two.choice == 'scissors' or self.player_two.choice == 'rock'):
                self.player_one.score += 1
                print(f'{self.player_one.name} score is {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is {self.player_two.score}')
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
            else:
                self.player_two.score += 1
                print(f'{self.player_one.name} score is {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is {self.player_two.score}')
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()

    def player_v_computer(self):
        self.player_h.choose_gesture()
        self.player_one.choose_gesture()
        while (self.player_h.score < 2) and (self.player_one.score < 2):
            if self.player_h.choice == self.player_one.choice:
                print('tie')
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player.name} score is {self.player_one.score}')
                self.player_h.choose_gesture()
                self.player_one.choose_gesture()
            elif self.player_h.choice == 'rock' and (self.player_one.choice == 'scissors' or self.player_one.choice == 'lizard'):
                self.player_h.score += 1
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player_one.name} score is {self.player_one.score}')
                self.player_h.choose_gesture()
                self.player_one.choose_gesture()
            elif self.player_h.choice == 'paper' and (self.player_one.choice == 'spock' or self.player_one.choice == 'rock'):
                self.player_h.score += 1
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player_one.name} score is {self.player_one.score}')
                self.player_h.choose_gesture()
                self.player_one.choose_gesture()
            elif self.player_h.choice == 'scissors' and (self.player_one.choice == 'paper' or self.player_one.choice == 'lizard'):
                self.player_h.score += 1  
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(1)
                print(f'{self.player_one.name} score is {self.player_one.score}')                       
                self.player_h.choose_gesture()
                self.player_one.choose_gesture()  
            elif self.player_h.choice == 'lizard' and (self.player_one.choice == 'spock' or self.player_one.choice == 'paper'):
                self.player_h.score += 1
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player_one.name} score is {self.player_one.score}')
                self.player_h.choose_gesture()
                self.player_one.choose_gesture()
            elif self.player_h.choice == 'spock' and (self.player_one.choice == 'scissors' or self.player_one.choice == 'rock'):
                self.player_h.score += 1
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player_one.name} score is {self.player_one.score}')
                self.player_h.choose_gesture()
                self.player_one.choose_gesture()
            else:
                self.player_one.score += 1
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player_one.name} score is {self.player_one.score}')
                self.player_h.choose_gesture()
                self.player_one.choose_gesture()

    def player_v_player(self):
        self.player_h.choose_gesture()
        self.player_h_two.choose_gesture()
        while (self.player_h.score < 2) and (self.player_h_two.score < 2):
            if self.player_h.choice == self.player_h_two.choice:
                print('tie')
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player.name} score is {self.player_h_two.score}')
                self.player_h.choose_gesture()
                self.player_h_two.choose_gesture()
            elif self.player_h.choice == 'rock' and (self.player_h_two.choice == 'scissors' or self.player_h_two.choice == 'lizard'):
                self.player_h.score += 1
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player_h_two.name} score is {self.player_h_two.score}')
                self.player_h.choose_gesture()
                self.player_h_two.choose_gesture()
            elif self.player_h.choice == 'paper' and (self.player_h_two.choice == 'spock' or self.player_h_two.choice == 'rock'):
                self.player_h.score += 1
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player_h_two.name} score is {self.player_h_two.score}')
                self.player_h.choose_gesture()
                self.player_h_two.choose_gesture()
            elif self.player_h.choice == 'scissors' and (self.player_h_two.choice == 'paper' or self.player_h_two.choice == 'lizard'):
                self.player_h.score += 1  
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(1)
                print(f'{self.player_h_two.name} score is {self.player_h_two.score}')                       
                self.player_h.choose_gesture()
                self.player_h_two.choose_gesture()  
            elif self.player_h.choice == 'lizard' and (self.player_h_two.choice == 'spock' or self.player_h_two.choice == 'paper'):
                self.player_h.score += 1
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player_h_two.name} score is {self.player_h_two.score}')
                self.player_h.choose_gesture()
                self.player_h_two.choose_gesture()
            elif self.player_h.choice == 'spock' and (self.player_h_two.choice == 'scissors' or self.player_h_two.choice == 'rock'):
                self.player_h.score += 1
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player_h_two.name} score is {self.player_h_two.score}')
                self.player_h.choose_gesture()
                self.player_h_two.choose_gesture()
            else:
                self.player_h_two.score += 1
                print(f'{self.player_h.name} score is {self.player_h.score}')
                #time.sleep(2)
                print(f'{self.player_h_two.name} score is {self.player_h_two.score}')
                self.player_h.choose_gesture()
                self.player_h_two.choose_gesture()





