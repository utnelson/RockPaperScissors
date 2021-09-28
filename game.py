# Schere, Stein, Papier
from player import HumanPlayer, AiPlayer


class RockPaperScissors:
    def __init__(self):
        self.table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
        self.game_map = {0: "rock", 1: "paper", 2: "scissors"}

    def check_win(self, p1_move, p2_move, print_game):
        winner = self.table[p1_move][p2_move]
        if winner == p1_move:
            if print_game:
                print("\nPlayer 1 wins!!!\n")
            return 1
        elif winner == p2_move:
            if print_game:
                print("\nPlayer 2 winns!!!\n")
            return 2
        else:
            if print_game:
                print("\nTie!!!\n")


def play(game, player1, player2, print_game):
    p1_move = player1.get_move()
    p2_move = player2.get_move()

    if print_game:
        print(f"Player 1 chosen: {game.game_map[p1_move]}\n"
              f"Player 2 chosen: {game.game_map[p2_move]}")

    result = r.check_win(p1_move, p2_move, print_game)
    return result


if __name__ == '__main__':
    r = RockPaperScissors()

    while True:
        mode = input(f"Rock Paper Scissors!\n"
                     f"1: Singleplayer\n"
                     f"2: Multiplayer\n"
                     f"3: Ai vs Ai for 1000 times\n"
                     f"q: Quit\n")

        if mode == "1":
            player1 = HumanPlayer()
            player2 = AiPlayer()
            play(r, player1, player2, print_game=True)

        if mode == "2":
            player1 = HumanPlayer()
            player2 = HumanPlayer()
            play(r, player1, player2, print_game=True)

        if mode == "3":
            player1 = AiPlayer()
            player2 = AiPlayer()
            p1_wins = 0
            p2_wins = 0
            ties = 0

            for _ in range(int(input("Round Count: "))):
                result = play(r, player1, player2, print_game=False)
                if result == 1:
                    p1_wins += 1
                elif result == 2:
                    p2_wins += 1
                else:
                    ties += 1
            print(f"Player 1 Win: {p1_wins}\n"
                  f"Player 2 Win: {p2_wins}\n"
                  f"Ties: {ties}\n")

        if mode == "q":
            break
