from pathlib import Path
from operator import add
from itertools import pairwise

class Maze(list):
    def __init__(self, l=[]):
        super().__init__(l)
        self.start = None

    def get(self, point):
        return self[point[0]][point[1]]
    
    def set(self, point, val):
        self[point[0]][point[1]] = val

maze = Maze()
with open(Path(__file__).parent / "data") as file:
    while line := file.readline().rstrip('\n'):
        maze.append(list(line))
        if not maze.start:
            try:
                c = line.index('S')
                maze.start = [len(maze) - 1, c]
            except ValueError:
                pass

move = {'N' : (-1,  0),
        'S' : (1, 0),
        'E' : (0,  1),
        'W' : (0, -1)}

orientation = { 'S': {           '|': 'S', 'L': 'E', 'J': 'W'},
                'N': { '|': 'N',           'F': 'E', '7': 'W'},
                'W': { 'L': 'N', 'F': 'S',           '-': 'W'},
                'E': { 'J': 'N', '7': 'S', '-': 'E',         }}

start = { 'NS': '|',
          'EW': '-',
          'ES': 'F',
          'SW': '7',
          'NW': 'J',
          'EN': 'L'}

def add_points(p1, p2):
    return list(map(add, p1, p2))

start_tile = []
for dir in ('N', 'S', 'E', 'W'):
    if orientation[dir].get(maze.get(add_points(maze.start, move[dir])), False):
        start_tile.append(dir)

maze.set(maze.start, start["".join(sorted(start_tile))])

boundary = [(maze.start, start_tile[0])]
while (next_position := add_points(boundary[-1][0], move[boundary[-1][1]])) != maze.start:
    boundary.append((next_position, orientation[boundary[-1][1]][maze.get(next_position)]))
print(f"Steps: {int(len(boundary)/2)}")

maze_clean = Maze([list('.' * len(row)) for row in maze])
for step in boundary:
    c = maze.get(step[0])
    if (c == '|' and step[1] == 'S') or (c == 'L' and step[1] == 'E') or (c == 'J' and step[1] == 'W'):
        maze_clean.set(step[0], '')
    elif (c == '|' and step[1] == 'N') or (c == 'L' and step[1] == 'N') or (c == 'J' and step[1] == 'N'):
        maze_clean.set(step[0], '')
    else:
        maze_clean.set(step[0], c)

inside = []
for row_idx, row in enumerate(maze_clean):
    crossings = 0
    for col_idx, tile in enumerate(row):
        c = maze_clean.get((row_idx, col_idx))
        if tile == '':
            crossings -= 1
        elif tile == '':
            crossings += 1
        elif tile == '.':
            if crossings:
                inside.append((row, tile))
                c = 'I'
print(f"Inside elements: {len(inside)}")
