# Terminal Python - CLI Mancala Game

A terminal-based implementation of the classic board game **Mancala** built using Python. This project simulates the traditional rules of Mancala, providing an interactive, text-based user interface that allows two players to play against each other in a command-line environment.

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [How to Play](#how-to-play)
4. [Installation](#installation)
5. [Project Structure](#project-structure)
6. [Key Code Highlights](#key-code-highlights)
7. [Contributing](#contributing)
8. [License](#license)

---

## Description

**Mancala** is one of the oldest and most well-known strategy games. It is traditionally played on a board with two rows of six pits, and the goal is to collect as many seeds as possible in your store. This Python project recreates the game of Mancala using object-oriented principles to manage the game state, handle player turns, and print a user-friendly board representation to the terminal.

The game logic is implemented through a set of classes and methods, allowing the player interaction to be smooth and intuitive. The program runs entirely in the terminal using basic input/output and includes clear, organized code to demonstrate **object-oriented programming (OOP)** skills and **CLI interaction**.

---

## Features

- **Two-player mode**: Allows two players to play alternately.
- **Interactive Command-Line Interface (CLI)**: Game interactions are handled through text input and output.
- **Game board display**: A simple, formatted display of the board after each move.
- **Input validation**: Ensures players can only make valid moves (selecting a pit with seeds).
- **Automatic winner detection**: The game automatically checks if a player has won or if there is a tie.

---

## How to Play

1. **Setup**: At the start of the game, players are prompted to enter their names. Each player controls one half of the board.
2. **Game Flow**: Players take turns picking one of their six pits and distributing the seeds in that pit across the board. If the last seed lands in their store, they get another turn. If the last seed lands in an empty pit on their side, they capture all seeds in the opposite pit.   
3. **End of Game*

## Run the Game
To start the game, run the mancala.py file:
    ```bash
    python3 mancala.py
    ```

## Project Structure
    ```bash
    mancala-python/
    │
    ├── mancala.py              # Main file to run the game
    ├── mancala_player.py       # Contains the Player class managing player data
    ├── terminal_board_print.py # Responsible for printing the game board
    └── README.md               # Project documentation
    ```

## Key Code Highlights:
- **Object-Oriented Design**: 
  - The `Player` class encapsulates all player-specific data, like their pits and store, which makes the game modular and easier to maintain.
  - The `Mancala` class orchestrates the gameplay, with clear methods for turn execution and winner detection.
  - 
- **Terminal I/O**: 
  - The game uses the terminal for both input and output, with clear and concise prompts for player actions, such as selecting a pit to "sow" seeds from.
  - The board is printed in an easy-to-read format after each move, providing a visual representation of the game state.


## Contributing
Contributions to improve the game are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a pull request to merge your changes into the main branch.

## License
This project is licensed under the MIT License.


# Docker for game_logic
1. Build the Docker image:
  ```bash
  docker build -t mancala-game .
  ```
2. Run the Docker container interactively:
  ```bash
  docker run -it mancala-game
  ```

# To run all three docker files (from project root):
  ```bash
  docker-compose up --build
  ```
