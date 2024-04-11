import pygame
import random
import math
from pygame.math import Vector2
pygame.init()
pygame.display.set_caption("Graphs")
gamescreen = pygame.display.set_mode ((900, 900))
tick = pygame.time.Clock()


# Add a vertex to the dictionary
def add_vertex(v):
  global graph
  global vertices_no
  randoming = Vector2(random.randrange(0, 880), random.randrange(0, 880))
  randoming2 = Vector2(random.randrange(0, 880), random.randrange(0, 880))
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    vertices_no = vertices_no + 1
    graph[v] = []
    pygame.draw.circle(gamescreen, (10, 255, 20), (randoming.x, randoming.y), 10)
    pygame.draw.circle(gamescreen, (10, 255, 20), (randoming2.x, randoming2.y), 10)
    pygame.draw.line(gamescreen, (255, 255, 255), (randoming.x, randoming.y), (randoming2.x, randoming2.y), 2)

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
  global graph
  # Check if vertex v1 is a valid vertex
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  # Check if vertex v2 is a valid vertex
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    pygame.draw.line(gamescreen, (255, 255, 255), (v1), (v2), e)
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    temp = [v2, e]
    graph[v1].append(temp)
    
    
    

# Print the graph
def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])
      

graph = {}
vertices_no = 0
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", graph)

# driver code

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Bye = True
    

    
   
    pygame.display.flip()
pygame.quit()
