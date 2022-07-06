from computer import Computer
from human import Human
#import #time #to slow down game

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        # self.player_h = Human('human one')
        # self.player_h_two = Human('humantwo')

    def run_game(self):
        self.get_rules()
        self.mode_select()
        self.end_message()
        
    def get_rules(self):
        print()
        print('Welcome to Rock Paper Scissor Lizard Spock')
        #time.sleep(1)
        print('Each match will be best of three')
        #time.sleep(1)
        print('The rules are simple...')
        #time.sleep(2)
        print(' Scissors cuts Paper')
        #time.sleep(1)
        print(' Paper covers Rock')
        #time.sleep(1)
        print(' Rock crushes Lizard')
        #time.sleep(1)
        print(' Spock smashes Scissors')
        #time.sleep(1)
        print(' Scissors decapitates Lizard')
        #time.sleep(1)
        print(' Lizard eats Paper')
        #time.sleep(1)
        print(' Spock vaporizes Rock')
        #time.sleep(1)
        print(' Paper disproves Spock')
        #time.sleep(1)
        print(' And as it always has, Rock crushes Scissors')

        print()
   
    
    def end_message(self):
        print('Thanks for playing! Have a great day!')

 
    def mode_select(self):
        game = True
        #time.sleep(1)
        game_choice = input('Press 1 for Human v Computer, 2 for Human v Human, 3 for a Surprise: ')
        while game == True:
            if game_choice == '1':
                self.player_one = Human('human one')
                self.player_two = Computer('Computer two')
                self.start_game()
                game = False
            elif game_choice == '2':
                self.player_one = Human('human one')
                self.player_two = Computer('robo one')                
                self.start_game()
                game = False
            elif game_choice == '3':
                self.player_one = Computer('robo one')
                self.player_two = Computer('robo two')
                self.start_game()
                game = False
            else:
                print('That is not a vaild option, try again.')
                game_choice = input('Press 1 for Human v Computer, 2 for Human v Human, 3 for a Suprise: ')

        
        
    def start_game(self):
        self.player_one.choose_gesture()
        #time.sleep(1)
        self.player_two.choose_gesture()
        while (self.player_one.score < 2) and (self.player_two.score < 2):
            if self.player_one.choice == self.player_two.choice:
                print('Tie! Go Again!')
                #time.sleep(1)
                print(f'{self.player_one.name} score is {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is {self.player_two.score}')
                #time.sleep(2)
                if self.player_one.score == 2 and self.player_two.score < 2:
                    print(f'{self.player_one.name} wins!')
                    break
                elif self.player_two.score == 2 and self.player_one.score < 2:
                    print(f'{self.player_two.name} wins!')
                    break
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
            elif self.player_one.choice == 'rock' and (self.player_two.choice == 'scissors' or self.player_two.choice == 'lizard'):
                self.player_one.score += 1
                print(f'{self.player_one.name} score is: {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is: {self.player_two.score}')
                #time.sleep(2)
                if self.player_one.score == 2 and self.player_two.score < 2:
                    print(f'{self.player_one.name} wins!')
                    break
                elif self.player_two.score == 2 and self.player_one.score < 2:
                    print(f'{self.player_two.name} wins!')
                    break
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
            elif self.player_one.choice == 'paper' and (self.player_two.choice == 'spock' or self.player_two.choice == 'rock'):
                self.player_one.score += 1
                print(f'{self.player_one.name} score is: {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is: {self.player_two.score}')
                #time.sleep(2)
                if self.player_one.score == 2 and self.player_two.score < 2:
                    print(f'{self.player_one.name} wins!')
                    break
                elif self.player_two.score == 2 and self.player_one.score < 2:
                    print(f'{self.player_two.name} wins!')
                    break
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
            elif self.player_one.choice == 'scissors' and (self.player_two.choice == 'paper' or self.player_two.choice == 'lizard'):
                self.player_one.score += 1  
                print(f'{self.player_one.name} score is: {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is: {self.player_two.score}')
                #time.sleep(2)
                if self.player_one.score == 2 and self.player_two.score < 2:
                    print(f'{self.player_one.name} wins!')
                    break
                elif self.player_two.score == 2 and self.player_one.score < 2:
                    print(f'{self.player_two.name} wins!')
                    break                      
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()  
            elif self.player_one.choice == 'lizard' and (self.player_two.choice == 'spock' or self.player_two.choice == 'paper'):
                self.player_one.score += 1
                print(f'{self.player_one.name} score is: {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is: {self.player_two.score}')
                #time.sleep(2)
                if self.player_one.score == 2 and self.player_two.score < 2:
                    print(f'{self.player_one.name} wins!')
                    break
                elif self.player_two.score == 2 and self.player_one.score < 2:
                    print(f'{self.player_two.name} wins!')
                    break
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
            elif self.player_one.choice == 'spock' and (self.player_two.choice == 'scissors' or self.player_two.choice == 'rock'):
                self.player_one.score += 1
                print(f'{self.player_one.name} score is: {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is: {self.player_two.score}')
                #time.sleep(2)
                if self.player_one.score == 2 and self.player_two.score < 2:
                    print(f'{self.player_one.name} wins!')
                    break
                elif self.player_two.score == 2 and self.player_one.score < 2:
                    print(f'{self.player_two.name} wins!')
                    break
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
            else:
                self.player_two.score += 1
                print(f'{self.player_one.name} score is: {self.player_one.score}')
                #time.sleep(2)
                print(f'{self.player_two.name} score is: {self.player_two.score}')
                #time.sleep(2)
                if self.player_one.score == 2 and self.player_two.score < 2:
                    print(f'{self.player_one.name} wins!')
                    break
                elif self.player_two.score == 2 and self.player_one.score < 2:
                    print(f'{self.player_two.name} wins!')
                    break
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()

  