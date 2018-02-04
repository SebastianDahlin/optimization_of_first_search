import pygame
import sys
import random
import time

def possible_moves(p_x, p_y):
    '''This function checks that the p_x and p_y input are not next to a boarder'''
    possible = []
    if p_y < Y -1:
        possible.append('U')
    if p_y -1 >= 0:
        possible.append('D')
    if p_x < X -1:
        possible.append('R')
    if p_x -1 >= 0:
        possible.append('L')
    return(possible)

class Matrix():
    '''This class holds information about both the matrix and the player'''
    def __init__(self):
        self.player = [0, 0] # Start point for player
        print(self.player)
        self.goal = goal # The goal of the player
        print(self.goal)
        self.matrix = [[{'step_count': 0,
          'Blocked' : False,
          'fill': 0,
          'Visited' : False} for i in range(X)] for j in range(Y)]

    def get_best_move(self, p_x, p_y, possible):
        best_move = []
        if 'L' in possible and self.matrix[p_x-1][p_y]['Visited'] == False:
                best_move.append('L')
        if 'R' in possible and self.matrix[p_x+1][p_y]['Visited'] == False:
                best_move.append('R')
        if 'U' in possible and self.matrix[p_x][p_y+1]['Visited'] == False:
                best_move.append('U')
        if 'D' in possible and self.matrix[p_x][p_y-1]['Visited'] == False:
                best_move.append('D')
        return(best_move)


        #Methods
    def p_move(self):
        # Assign player coordinates to variables
        p_x = self.player[0]
        p_y = self.player[1]
        # Get possible moves for the player
        possible = possible_moves(p_x, p_y)
        # Get the best move for the player
        best_move = self.get_best_move(p_x, p_y, possible)
        # Select a best move if possible
        if len(best_move)>0:
            move = random.choice(best_move)
        # If no possible "best move" available, choose one at random from possible  
        else:
            move = random.choice(possible)
        if move == 'U':
            self.player[1] +=1
        if move == 'D':
            self.player[1] -= 1
        if move == 'R':
            self.player[0] += 1
        if move == 'L':
            self.player[0] -= 1
        #Set the visited to yes
        matrix.matrix[self.player[0]][self.player[1]]['Visited'] = True
        # New reassignment of p_x and P_y
        p_x, p_y = self.player[0], self.player[1]
        # Get all possible neighbours
        possible_sc = possible_moves(p_x, p_y)
        # Create a neighbour step count list
        neighbour_sc = []
        # If current position equals start set the step count to zero.
        ## QUP: Makke the statements below be more general
        if self.player == [0, 0]:
            matrix.matrix[p_x][p_y]['step_count'] = 0
        elif self.player == [1,0] or self.player == [0,1]:
            matrix.matrix[p_x][p_y]['step_count'] = 1
        else:
            if 'L' in possible_sc: 
                step_count = matrix.matrix[p_x-1][p_y]['step_count']
                if step_count > 0:
                    neighbour_sc.append(step_count)
            if 'R' in possible_sc:
                step_count = matrix.matrix[p_x+1][p_y]['step_count']
                if step_count >0:
                    neighbour_sc.append(step_count)
            if 'U' in possible_sc:
                step_count = matrix.matrix[p_x][p_y+1]['step_count']
                if step_count >0:
                    neighbour_sc.append(step_count)
            if 'D' in possible_sc:
                step_count = matrix.matrix[p_x][p_y-1]['step_count']
                if step_count > 0:
                    neighbour_sc.append(step_count)
            # Set own stepcount
            smallest = min(int(s) for s in neighbour_sc)
            matrix.matrix[self.player[0]][self.player[1]]['step_count'] = smallest + 1
            

def render():
    SCREEN.fill((255, 255, 255))
    step_x = round(500/X)
    step_y = round(500/Y)
    pygame.draw.rect(SCREEN, (100, 255, 100), (matrix.goal[0]*step_x+100, matrix.goal[1]*step_y+100, step_x, step_y))
    myfont = pygame.font.SysFont("arial", 20)
    for i in range(0, Y):
        for j in range(0, X):
            if matrix.matrix[i][j]['fill'] == 0:
                pygame.draw.rect(SCREEN, (0, 0, 0),(100+step_x*i, 100+step_y*j, step_x, step_y),1)
            if matrix.matrix[i][j]['fill'] == 1:
                pygame.draw.rect(SCREEN, (0, 0, 0),(100+step_x*i, 100+step_y*j, step_x, step_y))
            step_count = matrix.matrix[i][j]['step_count']
            if matrix.matrix[i][j]['fill'] == 0:
                label = myfont.render(str(step_count), 1, (0,0,0))
            if matrix.matrix[i][j]['fill'] == 1:
                label = myfont.render(str(step_count), 1, (255,255,255))
            SCREEN.blit(label, (90+round(step_x/2)+step_x*i, 100+step_y*j))
    pygame.draw.circle(SCREEN, (255, 0, 0), (matrix.player[0]*step_x+100+round(step_x/2), matrix.player[1]*step_y+100+round(step_y/2)), 10)
    pygame.display.flip()

#Main program
##--Init stuff--#
###--Define stuff--###
##Matrix size
X = 15
Y = 15
goal = [14, 14]
# Call this function so the Pygame library can initialize itself
pygame.init()
# Create an 700x700 sized screen
SCREEN = pygame.display.set_mode([700, 700])
# Set the title of the window
pygame.display.set_caption('Maze solver')
matrix = Matrix()
do_again = True
# Start by finding the goal and while doing so plotting the shortest amount of steps available to get to a coordinate
while do_again is True:
    matrix.p_move()
    render()
    if matrix.player == matrix.goal:
        print("The goal has been reached")
        tot_step = matrix.matrix[goal[0]][goal[1]]['step_count']
        print("The total amount of steps to reach goal is %s." % (tot_step))
        do_again = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
# Back track from goal to start
back_track = goal
while tot_step is not 0:
    if tot_step > 1:
        possible_bt = []
        neighbour_bt = []
        if back_track[1] < Y -1:
            possible_bt.append('U')
        if back_track[1] -1 >= 0:
            possible_bt.append('D')
        if back_track[0] < X -1:
            possible_bt.append('R')
        if back_track[0] -1 >= 0:
            possible_bt.append('L')
        found = False    
        while found is False:
            if 'L' in possible_bt: 
                step_count = int(matrix.matrix[back_track[0]-1][back_track[1]]['step_count'])
                if step_count == tot_step -1:
                    found = True
                    tot_step = tot_step - 1
                    back_track[0] = back_track[0] - 1
            if 'R' in possible_bt and found is False:
                step_count = matrix.matrix[back_track[0]+1][back_track[1]]['step_count']
                if step_count == tot_step -1:
                    found = True
                    tot_step = tot_step - 1
                    back_track[0] = back_track[0] + 1
            if 'U' in possible_bt and found is False:
                step_count = matrix.matrix[back_track[0]][back_track[1]+1]['step_count']
                if step_count == tot_step -1:
                    found = True
                    tot_step = tot_step - 1
                    back_track[1] = back_track[1] + 1
            if 'D' in possible_bt and found is False:
                step_count = matrix.matrix[back_track[0]][back_track[1]-1]['step_count']
                if step_count == tot_step -1:
                    found = True
                    tot_step = tot_step - 1
                    back_track[1] = back_track[1] - 1
    else:
        found = True
        back_track = [0, 0]
        tot_step = 0
    matrix.matrix[back_track[0]][back_track[1]]['fill'] = 1
    render()
        
time.sleep(15)

pygame.QUIT
print("The tests are over")
