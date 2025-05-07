# 🎮 Mancala Connect  

A **modern reimagining** of the classic board game **Mancala**, built using Python. Originally developed as a **terminal-based CLI game**, this project is now evolving into a **full-stack web application** powered by **FastAPI** and **Vue.js**, with **real-time online multiplayer** via WebSockets.  

This transition is a personal challenge to sharpen my skills in **modern web development, real-time communication, and API design**—while making Mancala more accessible and engaging than ever! 🌍  

---

## 📜 Table of Contents  
1. [Project Overview](#-project-overview)  
2. [Project Evolution](#-project-evolution)  
3. [Features](#-features)  
4. [How to Play](#-how-to-play)  
5. [Installation](#-installation)  
6. [Project Structure](#-project-structure)  
7. [Key Code Highlights](#-key-code-highlights)  
8. [Docker Setup](#-docker-setup)  
9. [Contributing](#-contributing)  
10. [License](#-license)  

---

## 🎯 Project Overview  

**Mancala Connect** started as a **command-line Python game**, allowing two players to compete locally in a simple terminal interface. Now, it's evolving into a **full-stack web application** with:  
- **🌐 Online multiplayer** via WebSockets  
- **⚡ FastAPI backend** for high-performance API interactions  
- **🎨 Vue.js frontend** for a sleek, interactive UI  
- **🐳 Dockerized deployment** for scalability  

This transformation pushes me to **learn, adapt, and innovate**—and I’m excited to see where it leads! 🚀  

---

## 🔄 Project Evolution  

### 🏗️ **Original Version**  
The project began as a **pure Python CLI game**, focusing on **object-oriented programming (OOP)** and **game logic**. Players could take turns, interact with the board, and receive real-time feedback—all within the terminal.  

### 🚀 **Motivation for Improvement**  
While the CLI version was a great exercise in **game logic and OOP principles**, it lacked **scalability** and **modern UI/UX**. I wanted to push myself further by integrating **web technologies** and **real-time multiplayer**, making the game more accessible and engaging.  

### 🔧 **Professional Rework**  
The project is now evolving into a **full-stack web application**, leveraging cutting-edge technologies:  
- **🖥️ Frontend:** Migrating to **Vue.js** for a sleek, interactive UI.  
- **⚙️ Backend:** Transitioning to **FastAPI**, a high-performance Python framework for API development.  
- **🔗 Multiplayer:** Implementing **WebSockets** for real-time online play.  
- **📦 Containerization:** Using **Docker** to streamline deployment and scalability.  

### 📈 **Impact**  
This transformation enhances the game's **accessibility, scalability, and interactivity**, while also allowing me to deepen my expertise in **modern web development, API design, and real-time communication**.  

---

## ✨ Features  

- **🎭 Two-player mode** – Play against a friend in a local match.  
- **🌍 Online multiplayer** – Compete with players worldwide via WebSockets.  
- **💻 Interactive Command-Line Interface (CLI)** – Simple text-based gameplay (legacy version).  
- **📊 Game board display** – A formatted board updates after each move.  
- **✅ Input validation** – Ensures players can only make valid moves.  
- **🏆 Automatic winner detection** – The game checks for a win or tie.  

---

## 🎲 How to Play  

1. **Setup** – Players enter their names at the start. Each player controls one half of the board.  
2. **Game Flow** – Players take turns selecting a pit and distributing seeds.  
   - If the last seed lands in their store, they get another turn.  
   - If the last seed lands in an empty pit on their side, they capture seeds from the opposite pit.  
3. **End of Game** – The game ends when one side is empty. The player with the most seeds wins!  

---

## ⚙️ Installation  

To start the game, clone the repository and run the Python script:  

```bash
git clone https://github.com/yourusername/mancala-connect.git
cd mancala-connect
python3 mancala.py
```

## 📂Project Structure
```bash
mancala-connect/
│
├── mancala.py              # Main file to run the game
├── mancala_player.py       # Contains the Player class managing player data
├── terminal_board_print.py # Responsible for printing the game board
└── README.md               # Project documentation
```

## 🔑 Key Code Highlights
- 🛠️ Object-Oriented Design
  - The Player class encapsulates player-specific data, making the game modular.
  - The Mancala class orchestrates gameplay, handling turns and winner detection.
- 📟 Terminal I/O
  - The game uses the terminal for input and output, with clear prompts for player actions.
  - The board is printed in an easy-to-read format after each move.
## 🐳 Docker Setup
- Run the game in a Docker container
1. Build the Docker image:
```bash
docker build -t mancala-game .
```
2. Run the container interactively:
```bash
docker run -it mancala-game
```
3. Run all three Docker services (from project root):
```bash
docker-compose up --build
```

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
```bash
git checkout -b feature-branch
```
3. Make your changes.
4. Commit your changes:
```bash
git commit -am "Add new feature"
```
5. Push to the branch:
```bash
git push origin feature-branch
```
6. Create a pull request to merge your changes into the main branch.

## 📜 License
This project is licensed under the **MIT License**.
Copyright © 2025 Samuel Berven
