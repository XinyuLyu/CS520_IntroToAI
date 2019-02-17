import pandas as pd
from PIL import Image
def printMaze(maze, cells):
    start = 0
    end = 1
    maxtime = 1
    finalresult = []
    while end < len(cells):
        if cells[start] != cells[end] and cells[start] == cells[start + 1]:
            start = end - 1
        elif cells[start] != cells[end] and cells[start] != cells[start + 1]:
            start += 1
            end += 1
        elif cells[start] == cells[end]:
            if end - start + 1 > maxtime:
                maxtime = end - start + 1
            end += 1
    for i in range(len(cells) - maxtime):
        if cells[i] == cells[i + maxtime - 1]:
            finalresult.append(cells[i])

    mazeDrown = Image.new('RGB', (len(maze[0]), len(maze)))
    mazeX = mazeDrown.load()
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                mazeX[j, i] = (255, 255, 255)
            else:
                mazeX[j, i] = (0, 0, 0)
    for i in cells:
        mazeX[i[1], i[0]] = (0, 191, 255)
    for i in finalresult:
        mazeX[i[1], i[0]] = (255, 0, 255)
    mazeDrown.show()

def generateMaze(data):
    maze = []
    for i in range(43):
        temp = []
        for j in data.loc[i]:
            temp2 = j
            for j2 in temp2:
                if j2 == 'G':
                    temp.append(0)
                else:
                    temp.append(int(j2))
        maze.append(temp)
    return maze
