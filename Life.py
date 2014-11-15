#!/usr/bin/python

import copy


class LifeMap:

    def __init__(self, dimension, life_map, toroidal):
        self.dimension = dimension
        self.current_map = life_map
        self.toroidal = toroidal

    def cell(self, row, col):
        if (row < 0) or (row >= self.dimension) or (col < 0) or (col >= self.dimension):
            return 0
        return self.current_map[row][col]

class Game:

    def __init__(self, dimension, life_map, toroidal=False):
        self.life_map = LifeMap(dimension, life_map, toroidal)

    def dimension(self):
        return self.life_map.dimension

    def current_map(self):
        return self.life_map.current_map

    def neighbours(self, row, col):
        neighbours = 0
        neighbours += self.life_map.cell(row-1, col-1)
        neighbours += self.life_map.cell(row-1, col)
        neighbours += self.life_map.cell(row-1, col+1)
        neighbours += self.life_map.cell(row,   col-1)
        neighbours += self.life_map.cell(row,   col+1)
        neighbours += self.life_map.cell(row+1, col-1)
        neighbours += self.life_map.cell(row+1, col)
        neighbours += self.life_map.cell(row+1, col+1)
        return neighbours

    def next_status(self, row, col):
        neighbours = self.neighbours(row, col)
        if neighbours < 2 or neighbours > 3:
            return 0
        if neighbours == 2:
            return self.life_map.cell(row, col)
        return 1

    def next_life_map(self):
        life_map = copy.deepcopy(self.life_map.current_map)
        for row in range(self.dimension()):
            for col in range(self.dimension()):
                life_map[row][col] = self.next_status(row, col)
        self.life_map.current_map = life_map
        return self.life_map.current_map

