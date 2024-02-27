# Mancala
Basic logic for the game mancala, written in Python.

# Description: A recreation of the game Mancala. Includes two classes: Player and Mancala
#              In addition to initializing the Player object and associated data members, the Player class
#              also includes methods for getting and setting pits and stores, as well as for getting the player name.
#              The Mancala class also initializes the board and dictionary of (two) players. It also includes methods
#              for creating players, returning the player dictionary, printing the board, and returning the winner,
#              as well as the main method for playing the game itself.
#              The main Mancala.play_game() method is a bit unwieldy, but I found that ultimately it was smoother
#              than using helper functions.


TODO shortterm:
    refactor:
        print_board()
        execute_turn()
        return_winner()




    - Player name input authentication (have a character limit, and display this in the printing function, using regex to create an alignment buffer)
    - move input authentication  
    - Refactor code
    - Add player name references (instead of to just 'player 1' and 'player 2')
    - rename "play_string", as the 'string' part of the name is potentially misleading

TODO midterm:
    - Add gui (using TKinter or qt)
    - JS version (TS ultimately)
    - C# version

TODO longterm:
    - Refactor code
    - C version



