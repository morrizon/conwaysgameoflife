#!/usr/bin/python

import Life
import unittest

class TestLifeGame(unittest.TestCase):

    def setUp(self):
        self.raw_grid = [ [0, 0, 0, 0, 0], \
                          [0, 1, 1, 0, 0], \
                          [0, 1, 1, 0, 0], \
                          [0, 0, 0, 0, 0], \
                          [0, 0, 0, 0, 0]]
        self.raw_grid2 = [ [0, 0, 0, 0, 0], \
                           [0, 0, 1, 0, 0], \
                           [0, 0, 0, 1, 0], \
                           [0, 1, 0, 0, 0], \
                           [0, 0, 0, 0, 0]]
        self.next_raw_grid2 = [ [0, 0, 0, 0, 0], \
                                [0, 0, 0, 0, 0], \
                                [0, 0, 1, 0, 0], \
                                [0, 0, 0, 0, 0], \
                                [0, 0, 0, 0, 0]]
        self.game = Life.Game(self.raw_grid)
        self.game2 = Life.Game(self.raw_grid2)

    def test_raw_grid(self):
        self.assertEqual(self.raw_grid, self.game.raw_grid())

    def test_neighbours(self):
        self.assertEqual(1, self.game.neighbours(0, 0))
        self.assertEqual(3, self.game.neighbours(2, 1))
        self.assertEqual(3, self.game.neighbours(1, 2))
        self.assertEqual(0, self.game.neighbours(4, 4))

    def test_next_status(self):
        self.assertEqual(0, self.game.next_status(0, 0))
        self.assertEqual(1, self.game.next_status(1, 1))
        self.assertEqual(1, self.game.next_status(1, 2))
        self.assertEqual(0, self.game.next_status(4, 4))

    def test_next_step(self):
        self.assertEqual(self.raw_grid, self.game.next_step())
        self.assertEqual(self.raw_grid, self.game.raw_grid())
        self.assertEqual(self.next_raw_grid2, self.game2.next_step())
        self.assertEqual(self.next_raw_grid2, self.game2.raw_grid())

    def test_cell_value(self):
        is_life = 1
        self.assertEqual("\033[0;42m  \033[0m", self.game.cell(is_life))
        is_life = 0
        self.assertEqual("\033[30;47m  \033[0m", self.game.cell(is_life))

    def test_grid_total_rows(self):
        grid = Life.Grid(self.raw_grid)
        self.assertEqual(5, grid.total_rows())

    def test_grid_total_columns(self):
        grid = Life.Grid(self.raw_grid)
        self.assertEqual(5, grid.total_columns())
