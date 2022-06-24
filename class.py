


# rock crushes scissors-
# rock crushes lizard-
# paper disproves spock-
# paper covers rock-
# scissors cuts paper-
# scissors decapitates lizard
# lizard poisons spock-
# lizard eats paper-
# spock smashes scissors-
# spock vaporizes rock-

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

