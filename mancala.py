import sys
from terminal_board_print import print_board as display_board
from mancala_player import Player

class Mancala:
    """
    Represents Mancala game as played. Includes board (as a list), dictionary of Player objects, and methods for
    creating players, printing the board, checking if the game is over (and if it is, what the outcome is),
    generating the string to be used for play,
    and for using that string (after manipulation) to update Player data members
    """
    def __init__(self):
        self._players = {}
        self.create_player(input("Please enter Player 1's name: "), "Player 1", 0)
        self.create_player(input("Please enter Player 2's name: "), "Player 2", 7)

        self._board = self._players["Player 1"].get_pits_and_store() + self._players["Player 2"].get_pits_and_store()
        play_string = self.get_players()["Player 1"].get_pits_and_store() + self.get_players()[
            "Player 2"].get_pits_and_store()
        
        current_player = "Player 1"
        finished = False
        while not finished:
            # display_board(play_string)    
            display_board(play_string, self._players["Player 1"].get_name(), self._players["Player 2"].get_name())    
            self.execute_turn(current_player, play_string)

    def get_players(self):
        """
        Returns dictionary of Players
        """
        return self._players

    # TODO add in "offset" code explanation 
    def create_player(self, player_name, player_pos, offset):
        """
        Takes player name and offset as parameters and returns Player object
        """
        self._players[player_pos] = Player(player_name, offset)
        return self._players[player_pos]        

    def execute_turn(self, current_player, play_string):
        """
        Follows standard rules of Mancala, with two special rules:
        1) if the last seed falls in the player's store, then they may take another turn, and
        2) if the last seed falls in a previously empty pit on the player's side, that seed and all others in the
        opposite pit (so, on the opponent's side) are placed in the player's store.
        """
        self.return_winner()
        # print_board(play_string)

        if self.return_winner() != "The match continues!":
            print("Game is ended")

        offset = self.get_players()[current_player].get_offset()
        own_store = 6 + offset
        opponent_store = 13 - offset

        input_finished = False
        while input_finished is False: # TODO: refactor to something more obvious
            # pit_index = int(input(f"Choose your pit (1 through 6), {current_player}: "))
            pit_index = int(input(f"Choose your pit 1 through 6, {self._players[current_player].get_name()} ({current_player}): "))

            # factors in offset
            current_pos = (pit_index - 1) + offset

            if pit_index > 6 or pit_index <= 0:
                print("Not a valid pit. Please enter again. ")
            # case: no stones in selected pit
            elif play_string[current_pos] == 0:
                print("Play invalid: no stones in pit")
            else: input_finished = True

        while current_pos > 13:  # forces the current_pos to wrap around the play_string
            current_pos -= 13


        seeds_to_distribute = play_string[current_pos]
        play_string[current_pos] = 0
        # current_pos += 1

        while seeds_to_distribute >= 1:
            # NOTE nested whiles seems inefficient
            current_pos += 1
            if current_pos == opponent_store:
                current_pos += 1

            while current_pos > 13:  # forces the current_pos to wrap around the play_string
                current_pos -= 13

            if seeds_to_distribute == 1:
                # NOTE make the two special rules two different functions intead 
                if current_pos == own_store: # NOTE first special rule
                    # current_pos += 1
                    seeds_to_distribute -= 1
                    play_string[own_store] += 1
                    # display_board(play_string)
                    display_board(play_string, self._players["Player 1"].get_name(), self._players["Player 2"].get_name())
                    print(f"{current_player} take another turn")
                    self.execute_turn(current_player, play_string)
                elif play_string[current_pos] == 0: # NOTE second special rule
                    seeds_to_distribute -= 1
                    play_string[own_store] += play_string[13 - current_pos]
                    play_string[13 - current_pos] = 0
                else:
                    seeds_to_distribute -= 1
                    play_string[current_pos] += 1
            else:
                seeds_to_distribute -= 1
                play_string[current_pos] += 1

        # NOTE it seems like I can get around having to do this
        self.get_players()["Player 1"].set_pits_and_store(play_string[0:7:])
        self.get_players()["Player 2"].set_pits_and_store(play_string[7:14:])

        display_board(play_string, self._players["Player 1"].get_name(), self._players["Player 2"].get_name())
        
        # TODO there has to be a cleaner way to just switch between these
        if current_player == "Player 1":
            self.execute_turn("Player 2", play_string)
        else:
            self.execute_turn("Player 1", play_string)

    def return_winner(self):
        """
        If the game is ended, returns the winner in this format:
        “Winner is Player 1 (or 2, based on the actual winner): player’s name”
        If the game is a tie, return "It's a tie";
        If the game is not ended yet, return "Game has not ended".
        """
        p1_score = self.get_players()["Player 1"].get_store()
        p2_score = self.get_players()["Player 2"].get_store()

        if p1_score + p2_score < 48:
            return "The match continues!"
        else:    
            if p1_score == p2_score:
                print("It's a tie")
            elif p1_score > p2_score:
                print(f'Winner is Player 1: {self._players["Player 1"].get_name()}')
            elif p1_score < p2_score:
                print(f'Winner is Player 2: {self._players["Player 2"].get_name()}')
            self.finished = True
            sys.exit()


def main():
    game = Mancala()

if __name__ == "__main__":
    main()
