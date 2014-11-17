#!/usr/bin/python

import copy


class LifeMap:

    def __init__(self, life_map, toroidal=False):
        self.current_map = life_map
        self.toroidal = toroidal

    def cell(self, row, col):
        if (row < 0) or (row >= self.total_rows()) or (col < 0) or (col >= self.total_cols()):
            return 0
        return self.current_map[row][col]

    def total_rows(self):
        return len(self.current_map)

    def total_cols(self):
        return len(self.current_map[0])

class Game:

    def __init__(self, life_map, toroidal=False):
        self.life_map = LifeMap(life_map, toroidal)

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
        for row in range(self.life_map.total_rows()):
            for col in range(self.life_map.total_cols()):
                life_map[row][col] = self.next_status(row, col)
        self.life_map.current_map = life_map
        return self.life_map.current_map

    def cell(self, is_life):
        if is_life == 1:
            return "\033[0;42m  \033[0m"
        else:
            return "\033[30;47m  \033[0m"

    def show_current_map(self, separator=' '):
        output = ''
        output += '  ' + (separator.join('--' for cell in self.life_map.current_map[0])) + "\n"
        for row in self.life_map.current_map:
            output += '  ' + (separator.join(self.cell(is_life) for is_life in row)) + "\n"
        output += '  ' + (separator.join('--' for cell in self.life_map.current_map[0])) + "\n"
        return output
