#!/usr/bin/python

import copy

class Universe:

    def __init__(self, raw_universe, toroidal=False):
        self.raw_universe = raw_universe
        self.toroidal = toroidal

    def cell(self, row, column):
        if (row < 0) or (row >= self.total_rows()) or (column < 0) or (column >= self.total_columns()):
            return 0
        return self.raw_universe[row][column]

    def total_rows(self):
        return len(self.raw_universe)

    def total_columns(self):
        return len(self.raw_universe[0])

class Game:

    def __init__(self, raw_universe, toroidal=False):
        self.universe = Universe(raw_universe, toroidal)

    def raw_universe(self):
        return self.universe.raw_universe

    def neighbours(self, row, column):
        neighbours = 0
        neighbours += self.universe.cell(row-1, column-1)
        neighbours += self.universe.cell(row-1, column)
        neighbours += self.universe.cell(row-1, column+1)
        neighbours += self.universe.cell(row,   column-1)
        neighbours += self.universe.cell(row,   column+1)
        neighbours += self.universe.cell(row+1, column-1)
        neighbours += self.universe.cell(row+1, column)
        neighbours += self.universe.cell(row+1, column+1)
        return neighbours

    def next_status(self, row, column):
        neighbours = self.neighbours(row, column)
        if neighbours < 2 or neighbours > 3:
            return 0
        if neighbours == 2:
            return self.universe.cell(row, column)
        return 1

    def next_step(self):
        raw_universe = copy.deepcopy(self.universe.raw_universe)
        for row in range(self.universe.total_rows()):
            for column in range(self.universe.total_columns()):
                raw_universe[row][column] = self.next_status(row, column)
        self.universe.raw_universe = raw_universe
        return self.universe.raw_universe

    def cell(self, is_life):
        if is_life == 1:
            return "\033[0;42m  \033[0m"
        else:
            return "\033[30;47m  \033[0m"

    def show_universe(self, separator=' '):
        output = ''
        output += '  ' + (separator.join('--' for cell in self.universe.raw_universe[0])) + "\n"
        for row in self.universe.raw_universe:
            output += '  ' + (separator.join(self.cell(is_life) for is_life in row)) + "\n"
        output += '  ' + (separator.join('--' for cell in self.universe.raw_universe[0])) + "\n"
        return output
