#!/usr/bin/python

import GameOfLife
import unittest

class TestLifeGame(unittest.TestCase):

    def setUp(self):
        self.raw_universe = [ [0, 0, 0, 0, 0], \
                          [0, 1, 1, 0, 0], \
                          [0, 1, 1, 0, 0], \
                          [0, 0, 0, 0, 0], \
                          [0, 0, 0, 0, 0]]
        self.raw_universe2 = [ [0, 0, 0, 0, 0], \
                           [0, 0, 1, 0, 0], \
                           [0, 0, 0, 1, 0], \
                           [0, 1, 0, 0, 0], \
                           [0, 0, 0, 0, 0]]
        self.next_raw_universe2 = [ [0, 0, 0, 0, 0], \
                                [0, 0, 0, 0, 0], \
                                [0, 0, 1, 0, 0], \
                                [0, 0, 0, 0, 0], \
                                [0, 0, 0, 0, 0]]
        self.game = GameOfLife.Game(self.raw_universe)
        self.game2 = GameOfLife.Game(self.raw_universe2)

    def test_raw_universe(self):
        self.assertEqual(self.raw_universe, self.game.raw_universe())

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
        self.assertEqual(self.raw_universe, self.game.next_step())
        self.assertEqual(self.raw_universe, self.game.raw_universe())
        self.assertEqual(self.next_raw_universe2, self.game2.next_step())
        self.assertEqual(self.next_raw_universe2, self.game2.raw_universe())

    def test_cell_value(self):
        is_life = 1
        self.assertEqual("\033[0;42m  \033[0m", self.game.cell(is_life))
        is_life = 0
        self.assertEqual("\033[30;47m  \033[0m", self.game.cell(is_life))

    def test_universe_total_rows(self):
        universe = GameOfLife.Universe(self.raw_universe)
        self.assertEqual(5, universe.total_rows())

    def test_universe_total_columns(self):
        universe = GameOfLife.Universe(self.raw_universe)
        self.assertEqual(5, universe.total_columns())
