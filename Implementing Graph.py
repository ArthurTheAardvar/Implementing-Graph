import pygame
import random
import math
from pygame.math import Vector2
from random import randint as rr
pygame.init()
pygame.display.set_caption("Graphs")

SCREEN_SIZE = Vector2(900, 900)
gamescreen = pygame.display.set_mode(SCREEN_SIZE)
tick = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = font.render('This is what you get Mo ', False, (0,200, 200))



# Add a vertex to the dictionary

class Vertexes():
    def add_vertex(v: int):
        global graph
        global vertices_no
        if v in graph:
            print("Vertex ", v, " already exists.")
        else:
            vertices_no = vertices_no + 1
            graph[v] = []
    
        
class Edges():
    def add_edge(v1, v2, e):
        global graph
        # Check if vertex v1 is a valid vertex
        if v1 not in graph:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v2 is a valid vertex
        elif v2 not in graph:
            print("Vertex ", v2, " does not exist.")
        else:
            # Since this code is not restricted to a directed or 
            # an undirected graph, an edge between v1 v2 does not
            # imply that an edge exists between v2 and v1
            temp = [v2, e]
            graph[v1].append(temp)
            
    
       

    # Print the graph

                
graph:  dict[int, list[list[int]]] = {}

vertices_no = 0
Vertexes.add_vertex(1)
Vertexes.add_vertex(2)
Vertexes.add_vertex(3)
Vertexes.add_vertex(4)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
Edges.add_edge(1, 2, 1)
Edges.add_edge(1, 3, 1)
Edges.add_edge(2, 3, 3)
Edges.add_edge(3, 4, 4)
Edges.add_edge(4, 1, 5)

# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print (graph)

# driver code

def main():
    
    positions: list[Vector2] = []
    for i in graph:
        positions.append(Vector2(random.randrange(850), random.randrange(850)))

    # main loop:
    over = True
    while over:
    #delta = clock.tick(FRAMERATE) / 1000

    # input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = False

    # draw:
        gamescreen.fill("#000000")
        for i in graph:
            pygame.draw.circle(gamescreen, (rr(0,255), rr(0,255), rr(0,255)), positions[i-1], 10) 
            vertex = font.render(str(i), True, (255, 125, 0))
            gamescreen.blit(vertex, positions[i-1] + Vector2(5, 10))


        for t in graph:
            for g in graph[t]:
                startingpos =positions[t-1]
                endingpos =  positions[g[0]-1]
                length = startingpos.distance_to(endingpos)
                scaledlength = int(length / SCREEN_SIZE.length() * 255)
                r = scaledlength
                b= 255 - scaledlength
                gre = 125
                text = font.render(str(int(length)), True, (r, gre, b))
                midpoint = (startingpos + endingpos) / 2
        
                gamescreen.blit(text,midpoint)
                pygame.draw.line(gamescreen, (r, gre, b), startingpos, endingpos)
        
        pygame.display.flip()
if __name__ == "__main__":
   main() #thanks tam





