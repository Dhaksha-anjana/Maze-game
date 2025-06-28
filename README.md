🧠 Maze Game: Human vs AI (A* Pathfinding with Sound Effects)
A Python-based interactive maze game using Turtle, Tkinter, Pygame, and A* Algorithm. This project pits a human player (keyboard-controlled) against an AI bot that finds the shortest path to the goal using the A* pathfinding algorithm. The game includes movement history tracking, hit counters, and sound effects for both wall hits and victory.

📌 Features
🕹 Keyboard Controls (WASD or Arrow Keys)

🤖 AI Bot Navigation via A* pathfinding algorithm

🎯 Goal-Oriented Game: Both players race to reach the same goal

🔊 Sound Effects:

hit.wav: plays when a player hits a wall

win.wav: plays when a player reaches the goal

🧱 Maze Visualization using turtle graphics

📊 Live Movement & Hit History shown on screen

🧠 Simple Heuristic (Manhattan distance) for A* pathfinding

🖼 Game Overview
Human starts at top-left corner (0, 0)

AI starts at top-right corner (0, 9)

Goal is at bottom-right corner (9, 9)

Black tiles = walls (1 in the matrix)

White tiles = paths (0 in the matrix)

▶️ How to Play
Make sure you have Python 3.x installed.

Place hit.wav and win.wav files in the same directory.

Run the script:

bash
Copy code
python maze_game.py
Use Arrow Keys or WASD to move your player.

Avoid hitting walls — each hit is recorded!

First to reach the goal wins!

🛠 Requirements
Install required Python modules if not already present:

bash
Copy code
pip install pygame
turtle and tkinter come pre-installed with standard Python distributions.

🧩 Code Structure & Key Components
Component	Description
maze[][]	2D matrix representing the game maze (0 = path, 1 = wall)
astar()	Implements A* pathfinding for AI to reach the goal optimally
draw_maze()	Uses Turtle to draw the visual grid of the maze
Game class	Core game logic: handles movement, updates, AI steps, sound, and end check
update_history()	Displays move history and wall hit count
pygame.mixer.Sound()	Loads and plays sound effects on wall hit and game win
turtle.Screen()	Sets up the graphics window
tkinter.messagebox	Pops up a message box at the end of the game to show result summary

📷 Screenshots (Optional)
(Insert screenshots here showing gameplay and turtle window if you want to add them to GitHub)

📦 Folder Structure
bash
Copy code
maze_game/
│
├── maze_game.py         # Main Python script
├── hit.wav              # Wall hit sound
├── win.wav              # Victory sound
└── README.md            # Game instructions and overview
🙌 Acknowledgments
Python Turtle – for the graphics

Pygame – for audio effects

Tkinter – for dialog boxes

Heapq – for priority queue used in A*

