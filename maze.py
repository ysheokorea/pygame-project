#############################
# Python maze programming
# using pygame for animation
# ysheokorea
# pyhton 3.9.7
# 21.09.26
#############################


import pygame
import time
import random


#set up pygame window
WIDTH = 500
HEIGHT = 600
FPS = 30

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)

#initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("python maze program")
clock = pygame.time.Clock()

# setup maze global variables
x = 0
y = 0
w = 20
grid = []
visited = []
stack = []
solution = {}

def build_grid(x, y, w):
    for i in range(1,21):
        x = 20
        y = y + 20
        for j in range(1, 21):
            pygame.draw.line(screen, WHITE, [x,y], [x+w, y])        #top of cell
            pygame.draw.line(screen, WHITE, [x+w, y], [x+w, y+w])   #right of cell
            pygame.draw.line(screen, WHITE, [x+w, y+w], [x, y+w])   #bottom of cell
            pygame.draw.line(screen, WHITE, [x,y+w], [x, y])        #left of cell
            grid.append((x,y))
            x = x + 20                                              #move cell to new position
            

#Draw a rctangle twice the width of the cell
#pygame.draw.rect(Surface, color, Rect, Width=0)
def push_up(x, y):
    pygame.draw.rect(screen, BLUE, (x+1, y-w+1, 19,39), 0 )
    pygame.display.update()

def push_down(x, y):
    pygame.draw.rect(screen, BLUE, (x+1 , y+1, 19, 39), 0)
    pygame.display.update()

def push_left(x, y):
    pygame.draw.rect(screen, BLUE, (x-w+1, y+1, 39, 19), 0)
    pygame.display.update()

def push_right(x, y):
    pygame.draw.rect(screen, BLUE, (x+1, y+1, 39, 19), 0)
    pygame.display.update()

#Draw a single width cell
def single_cell(x, y):
    pygame.draw.rect(screen, GREEN, (x+1, y+1, 18, 18), 0)
    pygame.display.update()


# Re-color task after single_cell
def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x+1, y+1, 18, 18), 0)
    pygame.display.update()

# Show the solution
def solution_cell(x, y):
    pygame.draw.rect(screen, YELLOW, (x+8, y+8, 5, 5), 0)
    pygame.display.update()

def carve_out_maze(x, y):
    single_cell(x, y)                                           # starting positioning of maze
    stack.append((x, y))                                        # place starting cell into stack
    visited.append((x, y))                                      # Add starting cell to visited list

    while len(stack) != 0:                                      # Loop until stack is empty
        pygame.event.pump()                                     # Question to OS for every loop starting point / Not responding issue fixed
        time.sleep(0.01)                                        # slow a program now a bit
        
        cell = []                                               # define cell list
        # Right
        if (x + w, y) not in visited and (x + w, y) in grid:    # check if right cell available
            cell.append("right")                                # Add cell list
        # Left
        if (x - w, y) not in visited and (x - w, y) in grid:    # check if left cell available
            cell.append("left")
        # Donw            
        if (x, y + w) not in visited and (x, y + w) in grid:    # check if down cell available
            cell.append("down")
        # Up   
        if (x, y - w) not in visited and (x, y - w) in grid:    # check if up cell available
            cell.append("up")

        if len(cell) != 0:   
            cell_chosen = (random.choice(cell))                 # select one of the cell randomly

            if cell_chosen == "right":
                push_right(x, y)
                solution[(x + w, y)] = x, y
                x = x + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "left":
                push_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                solution[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                solution[(x, y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))

        else :
            x, y = stack.pop()          # if no cells available then pop one from the stack which is the latest cell chosen
            single_cell(x, y)           # use single_cell function to show backtracking image
            time.sleep(0.01)            # slow program down a bit
            backtracking_cell(x, y)     # Change color to green to identify backtracking path

def plot_route_back(x, y):
    solution_cell(x, y)         # solution list contains all the coordinates to route back to start
    while (x, y) != (20,20):    # Loop until cell position == start position
        pygame.event.pump()     # Question to OS for every loop starting point / Not responding issue fixed
        x, y = solution[(x, y)] # 'key value' now becomes the new key
        solution_cell(x, y)     # animate route back
        time.sleep(.3)

# pygame loop 
def main():
    
    running = True
    while running : 
        # keep running at the at the right spped
        clock.tick(FPS)
        # process input(evnets)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running : False

            x, y = 20, 20
            build_grid(40,0,20)
            carve_out_maze(x,y)
            plot_route_back(400,400)
            

# pygame starts form here
main()







