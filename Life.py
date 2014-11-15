#!/usr/bin/python

import copy

class Game:

    def __init__(self, dimension, life_map):
        self.dimension = dimension
        self.life_map = life_map

    def neighbours(self, row, col):
        neighbours = 0
        # above row
        if (row - 1) >= 0:
            if (col - 1) >= 0:
                neighbours += self.life_map[row-1][col-1]
            neighbours += self.life_map[row-1][col]
            if (col + 1) < self.dimension:
                neighbours += self.life_map[row-1][col+1]
        # middle row
        if (col - 1) >= 0:
            neighbours += self.life_map[row][col-1]
        if (col + 1) < self.dimension:
            neighbours += self.life_map[row][col+1]
        # below row
        if (row + 1) < self.dimension:
            if (col - 1) >= 0:
                neighbours += self.life_map[row+1][col-1]
            neighbours += self.life_map[row+1][col]
            if (col + 1) < self.dimension:
                neighbours += self.life_map[row+1][col+1]
        return neighbours

    def next_status(self, row, col):
        neighbours = self.neighbours(row, col)
        if neighbours < 2 or neighbours > 3:
            return 0
        if neighbours == 2:
            return self.life_map[row][col]
        return 1

    def next_life_map(self):
        life_map = copy.deepcopy(self.life_map)
        for row in range(self.dimension):
            for col in range(self.dimension):
                life_map[row][col] = self.next_status(row, col)
        self.life_map = life_map
        return self.life_map
