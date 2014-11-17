#!/usr/bin/python

import copy

class Grid:

    def __init__(self, raw_grid, toroidal=False):
        self.raw_grid = raw_grid
        self.toroidal = toroidal

    def cell(self, row, column):
        if (row < 0) or (row >= self.total_rows()) or (column < 0) or (column >= self.total_columns()):
            return 0
        return self.raw_grid[row][column]

    def total_rows(self):
        return len(self.raw_grid)

    def total_columns(self):
        return len(self.raw_grid[0])

class Game:

    def __init__(self, raw_grid, toroidal=False):
        self.grid = Grid(raw_grid, toroidal)

    def raw_grid(self):
        return self.grid.raw_grid

    def neighbours(self, row, column):
        neighbours = 0
        neighbours += self.grid.cell(row-1, column-1)
        neighbours += self.grid.cell(row-1, column)
        neighbours += self.grid.cell(row-1, column+1)
        neighbours += self.grid.cell(row,   column-1)
        neighbours += self.grid.cell(row,   column+1)
        neighbours += self.grid.cell(row+1, column-1)
        neighbours += self.grid.cell(row+1, column)
        neighbours += self.grid.cell(row+1, column+1)
        return neighbours

    def next_status(self, row, column):
        neighbours = self.neighbours(row, column)
        if neighbours < 2 or neighbours > 3:
            return 0
        if neighbours == 2:
            return self.grid.cell(row, column)
        return 1

    def next_step(self):
        raw_grid = copy.deepcopy(self.grid.raw_grid)
        for row in range(self.grid.total_rows()):
            for column in range(self.grid.total_columns()):
                raw_grid[row][column] = self.next_status(row, column)
        self.grid.raw_grid = raw_grid
        return self.grid.raw_grid

    def cell(self, is_life):
        if is_life == 1:
            return "\033[0;42m  \033[0m"
        else:
            return "\033[30;47m  \033[0m"

    def show_grid(self, separator=' '):
        output = ''
        output += '  ' + (separator.join('--' for cell in self.grid.raw_grid[0])) + "\n"
        for row in self.grid.raw_grid:
            output += '  ' + (separator.join(self.cell(is_life) for is_life in row)) + "\n"
        output += '  ' + (separator.join('--' for cell in self.grid.raw_grid[0])) + "\n"
        return output
