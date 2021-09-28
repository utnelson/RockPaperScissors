import random


class Player:
    def __init__(self):
        pass

    def get_move(self):
        pass


class HumanPlayer(Player):
    def __init__(self):
        super(HumanPlayer, self).__init__()

    def get_move(self):
        player_input = input("rock, paper or sciccors???\n")
        if player_input.lower() == "rock":
            player_move = 0
        elif player_input.lower() == "paper":
            player_move = 1
        elif player_input.lower() == "scissors":
            player_move = 2
        return player_move


class AiPlayer(Player):
    def __init__(self):
        super(AiPlayer, self).__init__()

    def get_move(self):
        player_move = random.randint(0, 2)
        return player_move
