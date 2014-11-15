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
        self.dimension = 5
        self.game = Life.Game(self.dimension, self.life_map)
        self.game2 = Life.Game(self.dimension, self.life_map2)

    def test_dimension(self):
        self.assertEqual(self.dimension, self.game.dimension)

    def test_life_map(self):
        self.assertEqual(self.life_map, self.game.life_map)

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
        self.assertEqual(self.life_map, self.game.life_map)
        self.assertEqual(self.next_life_map2, self.game2.next_life_map())
        self.assertEqual(self.next_life_map2, self.game2.life_map)
