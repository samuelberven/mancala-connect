import sys
from app.terminal_board_print import print_board as display_board
from app.mancala_player import Player

class Mancala:
    """
    Represents a Mancala game, including the board, players, and game logic.

    This class manages the game state, player turns, and rules of Mancala. It provides methods 
    for initializing players, making moves, printing the board, checking for game-over conditions, 
    and determining the winner.

    Attributes:
        board (list): The game board, containing pits and seeds.
        players (list): The list of players in the game.
        current_turn (int): Index of the player whose turn it is.

    Methods:
        create_players(): Initializes the players.
        print_board(): Displays the current state of the board.
        is_game_over(): Checks if the game has ended.
        determine_winner(): Determines the winner based on scores.
        make_move(player, pit_index): Executes a player's move.
        get_game_state(): Returns the current state of the game.
    """
    def __init__(self):
        """
        Todo: finish this docstring
        """
        self._players = {}

        # Todo: add in custom naming and validate_name() method later
        self.create_player("Player 1", "Player 1", 0)
        self.create_player("Player 2", "Player 2", 7)

        self._board = self._players["Player 1"].get_pits_and_store() + self._players["Player 2"].get_pits_and_store()

        # play_string = self.get_players()["Player 1"].get_pits_and_store() + self.get_players()[
        #     "Player 2"].get_pits_and_store()
        
        self.current_player = "Player 1"


        # finished = False
        # while not finished:
        #     # display_board(play_string)    
        #     display_board(play_string, self._players["Player 1"].get_name(), self._players["Player 2"].get_name())    
        #     self.execute_turn(current_player, play_string)

    # TODO add in "offset" code explanation 
    def create_player(self, player_name, player_pos, offset):
        """
        Takes player name and offset as parameters and returns Player object
        """
        self._players[player_pos] = Player(player_name, offset)
        return self._players[player_pos]        


    # def validate_name(self, player_num):
    #     while True:
    #         player_name = input(f"Please enter player {player_num}'s name (max 8 characters): ")
    #         if len(player_name) >= 8:
    #             print("Please enter a name with 8 or fewer characters: ")
    #         else:
    #             return player_name


    def get_players(self):
        """
        Returns dictionary of Players
        """
        return self._players

    def execute_turn(self, pit_index: int):
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

        offset = self.get_players()[self.current_player].get_offset()
        own_store = 6 + offset
        opponent_store = 13 - offset

        current_pos = (pit_index - 1) + offset

        if pit_index > 6 or pit_index <= 0:
            print("Not a valid pit. Please enter again. ")
        elif self._board[current_pos] == 0:
            print("Play invalid: no stones in pit")

        while current_pos > 13:  # forces the current_pos to wrap around the play_string
            current_pos -= 13

        seeds_to_distribute = self._board[current_pos]
        self._board[current_pos] = 0

        while seeds_to_distribute >= 1:
            # NOTE nested whiles seems inefficient
            current_pos += 1
            if current_pos == opponent_store:
                current_pos += 1

            while current_pos > 13:  # forces the current_pos to wrap around the play_string
                current_pos -= 13

            if seeds_to_distribute == 1:
                if current_pos == own_store:
                    self._board[own_store] += 1
                    return {"message": f"{self.current_player} gets another turn", "board": self._board}
                elif self._board[current_pos] == 0:
                    self._board[own_store] += self._board[13 - current_pos]
                    self._board[13 - current_pos] = 0

            self._board[current_pos] += 1
            seeds_to_distribute -= 1

        # NOTE it seems like I can get around having to do this
        self.get_players()["Player 1"].set_pits_and_store(self._board[0:7:])
        self.get_players()["Player 2"].set_pits_and_store(self._board[7:14:])

        # Swap players
        self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"

        return {"board": self._board, "current_player": self.current_player}

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
            return {"message": "The match continues!"}
        else:    
            if p1_score == p2_score:
                return {"message": "It's a tie"}
            elif p1_score > p2_score:
                return {"winner": f"Player 1 ({self._players['Player 1'].get_name()})"}
            elif p1_score < p2_score:
                return {"winner": f"Player 2 ({self._players['Player 2'].get_name()})"}
            self.finished = True
