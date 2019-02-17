from maze_helper import *

def move(maze, cells, action):
    if action == 'U':
        for cell in cells:
            if maze[cell[0] - 1][cell[1]] == 0:
                cell[0] -= 1
    elif action == 'D':
        for cell in cells:
            if maze[cell[0] + 1][cell[1]] == 0:
                cell[0] += 1
    elif action == 'L':
        for cell in cells:
            if maze[cell[0]][cell[1] - 1] == 0:
                cell[1] -= 1
    elif action == 'R':
        for cell in cells:
            if maze[cell[0]][cell[1] + 1] == 0:
                cell[1] += 1
    return cells

def get_blocks(maze, Observation):
    cells = []
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if getBlocksAround(x, y, maze) == Observation:
                cells.append([x, y])
    return cells


def Change(maze, Cel, Action, Obervation):
    cells1 = move(maze, Cel, Action)
    cells = []
    for cell in cells1:
        if getBlocksAround(cell[0], cell[1], maze) == Obervation:
            cells.append(cell)
    return cells

def getBlocksAround(X, Y, maze):
    blocks = 0
    if X == 0 or Y == 0 or X == 42 or Y == 56:
        return 0
    if maze[X][Y] == 1:
        return None
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            temp = maze[X + i][Y + j]
            if temp == 1:
                blocks += 1
    return blocks


def findProbability(cells):
    cell_str = []
    dict = {}
    for cell in cells:
        cell_str.append(str(cell))
    for i in cell_str:
        if i not in dict:
            dict[i] = 1 / len(cells)
        else:
            dict[i] += 1 / len(cells)
    dict = sorted(dict.items(), key=lambda k: k[1], reverse=True)
    return dict


if __name__ == '__main__':
    maze_data = pd.read_table("Maze.txt", header=None)
    Maze = generateMaze(maze_data)
    Observations = [5, 5, 5]
    Actions = ['L', 'L']
    Initial_cells = get_blocks(Maze, Observations[0])
    for i in range(len(Actions)):
        Initial_cells = Change(Maze, Initial_cells, Actions[i], Observations[i + 1])
    cell_count = findProbability(Initial_cells)
    print('possible positions and probability')
    print(cell_count)
    printMaze(Maze, Initial_cells)
