import unittest

from Colours import Colours
from Logic.Game import Game


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

    def test_winning(self):
        game = Game(2, 2)
        game.test_field()
        game.make_turn(Colours(2))
        self.assertTrue(game.is_win)

    def test_changing_colour(self):
        game = Game(3, 6)
        colour = game.active_nodes[0].colour
        if colour.value > 1:
            game.change_colour(Colours(int(colour.value) - 1))
        else:
            game.change_colour(Colours(int(colour.value) + 1))
        self.assertNotEqual(colour, game.active_nodes[0])

    def test_inc_turns(self):
        game = Game(3, 6)
        colour = game.active_nodes[0].colour
        turns = game.number_of_turns
        if colour.value > 1:
            game.make_turn(Colours(int(colour.value) - 1))
        else:
            game.make_turn(Colours(int(colour.value) + 1))
        self.assertNotEqual(turns, game.number_of_turns)

    def test_no_inc_turns(self):
        game = Game(3, 6)
        colour = game.active_nodes[0].colour
        turns = game.number_of_turns
        game.make_turn(colour)
        self.assertEqual(turns, game.number_of_turns)

    def test_set_active_nodes(self):
        game = Game(3, 2)
        colour = game.active_nodes[0].colour
        nodes = len(game.active_nodes)
        if colour.value > 1:
            game.make_turn(Colours(int(colour.value) - 1))
        else:
            game.make_turn(Colours(int(colour.value) + 1))
        self.assertNotEqual(nodes, len(game.active_nodes))


if __name__ == '__main__':
    unittest.main()
