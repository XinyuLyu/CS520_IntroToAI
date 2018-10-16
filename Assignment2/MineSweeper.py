import Grid
from Assignment2.Cell import *


class MineSweeper:
    def __init__(self):
        grid = Grid(9, 9, 0.1)
        print(1)

    def flagMines(self,grid):
        for i in range(grid.height):
            for j in range(grid.width):
                cell = grid.getCell(i,j)
                if not cell.isCovered:
                    numOfmines = cell.numOfMines
                    if numOfmines >= 1 and numOfmines == grid.numOfCoveredCell(i,j):
                        for ii in range(-1, 2):
                            for jj in range(-1, 2):
                                adj = grid.getCell(i + ii, j + jj)
                                if not adj.isOutside and adj.isCovered:
                                    adj.isFlag = True

    def drawGrid(self,grid):
        for cell in grid:
            for i in range(grid.height):
                for j in range(grid.width):
                    if grid.getCell(i,j):
                if cell.isMine == True:
                    print ("*")
                else:
                    print(cell.numOfMines)




    def clickCell(self, grid):
        flag = False

        for i in range(grid.borderHeight):
            for j in range(grid.borderWidth):

                curCell = grid.getCell(i, j)

                // if
                if not curCell.isCovered:
                    continue

                numOfMines = curCell.numOfMines
                numOfActualMines = grid.numOfFlags(i, j)
                numOfCoveredCell = grid.numOfCoveredCell(i, j)

                if numOfMines == numOfActualMines and numOfCoveredCell > 0:
                    for ii in range(-1, 2):
                        for jj in range(-1, 2):
                            adj = grid.getCell(i + ii, j + jj)
                            if not adj.isOutside and adj.isCovered:
                                 adj.isCovered = False



if __name__ == '__main__':
    print(1)
