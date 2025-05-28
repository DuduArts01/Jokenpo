from random import randint

class Logic_Game:
    def __init__(self, player):
        self.player = player

    def computer(self):
        number = randint(0,2)
        if number == 0:
            self.computer_value = "rock"
        elif number:
            self.computer_value = "paper"
        else:
            self.computer_value = "scissor"

    
    def checkWin(self):
        if self.player == self.computer_value:
            pass # Draw
        elif self.player == "rock" and self.computer_value == "paper":
            pass # Computer won
        elif self.player == "paper" and self.computer_value == "scissor":
            pass # Computer won
        elif self.player == "scissor" and self.computer_value == "rock":
            pass # Computer won
        else:
            pass # Player Won
        