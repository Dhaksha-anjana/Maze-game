import turtle 
import tkinter as tk 
from tkinter import messagebox 
import heapq 
import pygame  # Importing pygame for sound handling 
 
# Initialize pygame mixer 
pygame.mixer.init() 
 
# Load sound effects 
hit_sound = pygame.mixer.Sound("hit.wav") 
win_sound = pygame.mixer.Sound("win.wav") 
 
# Maze definition 
maze = [ 
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 
16 
 
 
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0], 
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0], 
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
] 
 
ROWS = len(maze) 
COLS = len(maze[0]) 
TILE_SIZE = 30  # Reduced tile size 
 
# Positions 
start_human = (0, 0) 
start_ai = (0,9) 
goal = (9, 9) 
 
# A* Algorithm 
def astar(start, goal, grid): 
    def heuristic(a, b): 
        return abs(a[0]-b[0]) + abs(a[1]-b[1]) 
     
    open_set = [] 
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start)) 
    came_from = {} 
    g_score = {start: 0} 
 
    while open_set: 
        _, cost, current = heapq.heappop(open_set) 
        if current == goal: 
            path = [] 
 
 
 
            while current in came_from: 
                path.append(current) 
                current = came_from[current] 
            return path[::-1] 
 
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]: 
            neighbor = (current[0] + dx, current[1] + dy) 
            if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS: 
                if grid[neighbor[0]][neighbor[1]] == 1: 
                    continue 
                tentative_g = g_score[current] + 1 
                if neighbor not in g_score or tentative_g < g_score[neighbor]: 
                    came_from[neighbor] = current 
                    g_score[neighbor] = tentative_g 
                    f_score = tentative_g + heuristic(neighbor, goal) 
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor)) 
    return [] 
 
# Turtle setup 
wn = turtle.Screen() 
wn.setup(COLS*TILE_SIZE + 250, ROWS*TILE_SIZE + 150) 
wn.title("Maze Game: Human vs AI (Keyboard Controlled)") 
wn.tracer(0) 
 
pen = turtle.Turtle() 
pen.hideturtle() 
pen.penup() 
 
def draw_maze(): 
    for r in range(ROWS): 
        for c in range(COLS): 
            x = c * TILE_SIZE - 200 
            y = -r * TILE_SIZE + 200 
            pen.goto(x, y) 
 
 
 
 
            if (r, c) == start_human: 
                pen.color("lightblue") 
            elif (r, c) == start_ai: 
                pen.color("lightcoral") 
            elif (r, c) == goal: 
                pen.color("lightgreen") 
            elif maze[r][c] == 1: 
                pen.color("black") 
            else: 
                continue 
 
            pen.begin_fill() 
            for _ in range(4): 
                pen.forward(TILE_SIZE) 
                pen.right(90) 
            pen.end_fill() 
 
draw_maze() 
 
# Text display 
text_writer = turtle.Turtle() 
text_writer.hideturtle() 
text_writer.penup() 
text_writer.color("black") 
 
def update_history(human_moves, ai_moves, human_hits, ai_hits): 
    text_writer.clear() 
    text_writer.goto(250, 180) 
    text_writer.write("Controls: Arrow Keys or W A S D", align="left", font=("Arial", 
10, "bold")) 
     
    text_writer.goto(250, 160) 
    text_writer.write("Move History:", align="left", font=("Arial", 10, "bold")) 
 
 
 
 
    start_y = 140 
    for i in range(max(len(human_moves), len(ai_moves))): 
        h_move = f"Human: {human_moves[i]}" if i < len(human_moves) else "" 
        a_move = f"AI: {ai_moves[i]}" if i < len(ai_moves) else "" 
        text_writer.goto(250, start_y - i * 18) 
        text_writer.write(f"{h_move:<15} {a_move}", align="left", font=("Arial", 10, 
"normal")) 
 
    text_writer.goto(250, start_y - (max(len(human_moves), len(ai_moves)) + 2) * 18) 
    text_writer.write(f"Hits - Human: {human_hits} | AI: {ai_hits}", align="left", 
font=("Arial", 12, "bold")) 
 
# Player turtles 
human = turtle.Turtle() 
human.shape("circle") 
human.color("blue") 
human.penup() 
human.goto(start_human[1]*TILE_SIZE - 200, -start_human[0]*TILE_SIZE + 200) 
 
ai = turtle.Turtle() 
ai.shape("square") 
ai.color("red") 
ai.penup() 
ai.goto(start_ai[1]*TILE_SIZE - 200, -start_ai[0]*TILE_SIZE + 200) 
 
# Game logic 
class Game: 
    def __init__(self): 
        self.human_pos = start_human 
        self.ai_pos = start_ai 
        self.ai_path = astar(start_ai, goal, maze) 
        self.ai_index = 0 
        self.human_hits = 0 
        self.ai_hits = 0 
 
 
 
        self.human_moves = [] 
        self.ai_moves = [] 
        self.game_over = False 
        update_history(self.human_moves, self.ai_moves, self.human_hits, self.ai_hits) 
        wn.listen() 
        self.bind_keys() 
 
    def bind_keys(self): 
        wn.onkey(lambda: self.handle_turn("up"), "Up") 
        wn.onkey(lambda: self.handle_turn("down"), "Down") 
        wn.onkey(lambda: self.handle_turn("left"), "Left") 
        wn.onkey(lambda: self.handle_turn("right"), "Right") 
        wn.onkey(lambda: self.handle_turn("up"), "w") 
        wn.onkey(lambda: self.handle_turn("down"), "s") 
        wn.onkey(lambda: self.handle_turn("left"), "a") 
        wn.onkey(lambda: self.handle_turn("right"), "d") 
 
    def handle_turn(self, direction): 
        if self.game_over: 
            return 
        self.move_human(direction) 
        self.move_ai() 
        update_history(self.human_moves, self.ai_moves, self.human_hits, self.ai_hits) 
        wn.update() 
        self.check_end() 
 
    def move_human(self, move): 
        directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)} 
        dr, dc = directions.get(move, (0, 0)) 
        nr, nc = self.human_pos[0] + dr, self.human_pos[1] + dc 
        self.human_moves.append(move) 
 
        if 0 <= nr < ROWS and 0 <= nc < COLS: 
            if maze[nr][nc] == 1: 
 
 
 
                self.human_hits += 1 
                hit_sound.play()  # Play the hit sound when human hits a wall 
            else: 
                self.human_pos = (nr, nc) 
                human.goto(nc*TILE_SIZE - 200, -nr*TILE_SIZE + 200) 
 
    def move_ai(self): 
        if self.ai_index < len(self.ai_path): 
            next_pos = self.ai_path[self.ai_index] 
            move_dir = self.get_direction(self.ai_pos, next_pos) 
            self.ai_moves.append(move_dir) 
            if maze[next_pos[0]][next_pos[1]] == 1: 
                self.ai_hits += 1 
                hit_sound.play()  # Play the hit sound when AI hits a wall 
            self.ai_pos = next_pos 
            ai.goto(next_pos[1]*TILE_SIZE - 200, -next_pos[0]*TILE_SIZE + 200) 
            self.ai_index += 1 
 
    def get_direction(self, from_pos, to_pos): 
        dr = to_pos[0] - from_pos[0] 
        dc = to_pos[1] - from_pos[1] 
        if dr == -1: return "up" 
        if dr == 1: return "down" 
        if dc == -1: return "left" 
        if dc == 1: return "right" 
        return "stay" 
 
    def check_end(self): 
        if self.human_pos == goal or self.ai_pos == goal: 
            self.game_over = True 
            if self.human_pos == goal or self.ai_pos == goal: 
                win_sound.play()  # Play the win sound when the game ends 
            msg = f"Hits - Human: {self.human_hits}, AI: {self.ai_hits}\n\n" 
            if self.human_pos == goal and self.ai_pos == goal: 

 
 
                msg += "    It's a tie! Both reached the goal!" 
            elif self.human_pos == goal: 
                msg += "              Human reached the goal first! You win!" 
            elif self.ai_pos == goal: 
                msg += "         AI reached the goal first. AI wins!" 
            messagebox.showinfo("Game Over", msg) 
            wn.bye() 
 
# Launch game 
game = Game() 
wn.mainloop()