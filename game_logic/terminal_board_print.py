import os

# def print_board(current_play_string):
def print_board(current_play_string, player1_name, player2_name):

    """
    Prints current board information, in the format of:
    player1: store: number of seeds in player 1’s store; player 1 seeds number from pit 1 to 6 in a list
    player2: store: number of seeds in player 2’s store; player 2 seeds number from pit 1 to 6 in a list
    """
    formatted_board = []
    for el in range(len(current_play_string)):
        if current_play_string[el] < 10:
            formatted_board.append(' ' + str(current_play_string[el]))
        else:
            formatted_board.append(str(current_play_string[el]))

    os.system('clear')

# Draw the top portion of the board (Player 2's pits and store)
    # print("\n\n")
    # print(f"   _    _                                                           ")
    # print(f"  | \\  / |                 _          |                             ")
    # print(f"  |  \\/  |   ___    __    / \\   ___   |     ___                     ")
    # print(f"  |      |  /   \\  |  \\  |     /   \\  |   /   \\                    ")
    # print(f"  |      |  \\___/\\ |   |  \\_/  \\___/\\ |   \\___/\\                   ")
    # print(f"")
    
    print("\n\n")
    print(f"  __  __                        _        ")
    print(f" |  \/  |                      | |       ")
    print(f" | \  / | __ _ _ __  ____  __ _| | __ _  ")
    print(f" | |\/| |/ _` | '_ \/  __|/ _` | |/ _` | ")
    print(f" | |  | | (_| | | | \ (__' (_| | | (_| | ")
    print(f" |_|  |_|\__,_|_| |_|\___|\__,_|_|\__,_| ")
    print(f"                                         ")

    # This limits player usernames to 8 characters

    print(f"+==========+====+====+====+====+====+====+==========+")
    print(f"| {player2_name:^8} | {formatted_board[12]:>2} | {formatted_board[11]:>2} | {formatted_board[10]:>2} | {formatted_board[9]:>2} | {formatted_board[8]:>2} | {formatted_board[7]:>2} | {player1_name:^8} |")
    print(f"|   {formatted_board[13]:>2}     |====+====+====+====+====+====|   {formatted_board[6]:>2}     |")

    # Middle line to separate pits and player banks visually
    print(f"|          | {formatted_board[0]:>2} | {formatted_board[1]:>2} | {formatted_board[2]:>2} | {formatted_board[3]:>2} | {formatted_board[4]:>2} | {formatted_board[5]:>2} |          |")

    # Bottom boundary and pits of Player 1
    print(f"+==========+====+====+====+====+====+====+==========+")

    # # Top boundary and pits of Player 2
    # print(f"+----------+----+----+----+----+----+----+----------+")
    # print(f"| {player2_name:^8} | {formatted_board[12]} | {formatted_board[11]} | {formatted_board[10]} | {formatted_board[9]} | {formatted_board[8]} | {formatted_board[7]} |  {player1_name:^8}|")
    # print(f"|    {formatted_board[13]}    +----+----+----+----+----+----+    {formatted_board[6]}    |")

    # # Bottom pits of Player 2 and Player 1
    # print(f"|          | {formatted_board[0]} | {formatted_board[1]} | {formatted_board[2]} | {formatted_board[3]} | {formatted_board[4]} | {formatted_board[5]} |          |")

    # # Bottom boundary and pits of Player 1
    # print(f"+----------+----+----+----+----+----+----+----------+")

    # Print a friendly match message
    print(f"\n{player2_name} vs. {player1_name}!")
    print("\n")

    # print("\n\n")
    # print(f"   _    _                                                             ")
    # print(f"  | \  / |                 _          |                               ")
    # print(f"  |  \/  |   ___    __    / \   ___   |     ___                       ")
    # print(f"  |      |  /   \  |  \  |     /   \  |   /   \                       ")
    # print(f"  |      |  \___/\ |   |  \_/  \___/\ |   \___/\                      ")
    # print(f"")
    # print(f"+----------+----+----+----+----+----+----+----------+")
    # print(f"| Player 2 | {formatted_board[12]} | {formatted_board[11]} | {formatted_board[10]} | {formatted_board[9]} | {formatted_board[8]} | {formatted_board[7]} | Player 1 |")
    # print(f"|    {formatted_board[13]}    +----+----+----+----+----+----+    {formatted_board[6]}    |")
    # print(f"|          | {formatted_board[0]} | {formatted_board[1]} | {formatted_board[2]} | {formatted_board[3]} | {formatted_board[4]} | {formatted_board[5]} |          |")
    # print(f"+----------+----+----+----+----+----+----+----------+")
    # print(f"{player2_name} vs. {player1_name}!")
    # print("\n")