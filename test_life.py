#!/usr/bin/python

import Life
import unittest

class TestLifeGame(unittest.TestCase):

    def setUp(self):
        self.life_map = [ [0, 0, 0, 0, 0], \
                          [0, 1, 1, 0, 0], \
                          [0, 1, 1, 0, 0], \
                          [0, 0, 0, 0, 0], \
                          [0, 0, 0, 0, 0]]
        self.life_map2 = [ [0, 0, 0, 0, 0], \
                           [0, 0, 1, 0, 0], \
                           [0, 0, 0, 1, 0], \
                           [0, 1, 0, 0, 0], \
                           [0, 0, 0, 0, 0]]
        self.next_life_map2 = [ [0, 0, 0, 0, 0], \
                                [0, 0, 0, 0, 0], \
                                [0, 0, 1, 0, 0], \
                                [0, 0, 0, 0, 0], \
                                [0, 0, 0, 0, 0]]
        self.game = Life.Game(self.life_map)
        self.game2 = Life.Game(self.life_map2)

    def test_life_map(self):
        self.assertEqual(self.life_map, self.game.current_map())

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

    def test_next_life_map(self):
        self.assertEqual(self.life_map, self.game.next_life_map())
        self.assertEqual(self.life_map, self.game.current_map())
        self.assertEqual(self.next_life_map2, self.game2.next_life_map())
        self.assertEqual(self.next_life_map2, self.game2.current_map())

    def test_cell_value(self):
        is_life = 1
        self.assertEqual("\033[0;42m  \033[0m", self.game.cell(is_life))
        is_life = 0
        self.assertEqual("\033[30;47m  \033[0m", self.game.cell(is_life))

    def test_life_map_total_rows(self):
        life_map = Life.LifeMap(self.life_map)
        self.assertEqual(5, life_map.total_rows())

    def test_life_map_total_cols(self):
        life_map = Life.LifeMap(self.life_map)
        self.assertEqual(5, life_map.total_cols())
