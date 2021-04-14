from Logic.Node import Node
from Colours import Colours
import random
import math


class Game:
    def __init__(self, field_size: int = 10, colour_number: int = 6):
        self.__field_size = field_size
        self.coeff = colour_number
        if colour_number > 4:
            self.coeff = 4
        self.optimal_turns_number = round(round(math.log2(field_size)) * self.coeff + 0.5)
        self.__colour_number = colour_number
        self.__active_nodes = []
        self.optimal_turns_number = self.find_optimal_turns()
        self.__new_active_nodes = []
        self.__initialize_field()
        self.__turns_counter = 0
        self.__cells_number = self.__field_size ** 2
        self.__is_win = False

    @property
    def field(self):
        return self.__field

    @property
    def number_of_turns(self):
        return self.__turns_counter

    @property
    def is_win(self):
        return self.__is_win

    @property
    def field_size(self):
        return self.__field_size

    @property
    def active_nodes(self):
        return self.__active_nodes

    def change_colour(self, colour: Colours):
        for obj in self.__active_nodes:
            obj.colour = colour

    def __set_new_active_nodes(self):
        for obj in self.__new_active_nodes:
            res = self.__get_neighbors_for(obj)
            self.__new_active_nodes.extend(res)
            self.__active_nodes.extend(res)
        temp_nodes = [item for item in self.__new_active_nodes if not self.is_all_neighbors_active(item)]
        self.__new_active_nodes = temp_nodes

    def __get_neighbors_for(self, node: Node):
        res = []
        x = node.x
        y = node.y
        if 0 < x and not self.__field[y][x - 1].is_active and self.__field[y][x - 1].colour == node.colour:
            res.append(self.__field[y][x - 1])
        if self.__field_size - 1 > x and not self.__field[y][x + 1].is_active and self.__field[y][
            x + 1].colour == node.colour:
            res.append(self.__field[y][x + 1])
        if 0 < y and not self.__field[y - 1][x].is_active and self.__field[y - 1][x].colour == node.colour:
            res.append(self.__field[y - 1][x])
        if self.__field_size - 1 > node.y and not self.__field[y + 1][x].is_active and self.__field[y + 1][
            x].colour == node.colour:
            res.append(self.__field[y + 1][x])
        for obj in res:
            obj.make_active()
        return res

    def is_all_neighbors_active(self, node: Node):
        x = node.x
        y = node.y
        res = True
        if x > 0:
            res = self.__field[y][x - 1].is_active
        if x < self.__field_size - 1 and res:
            res = self.__field[y][x + 1].is_active
        if y > 0 and res:
            res = self.__field[y - 1][x].is_active
        if y < self.__field_size - 1 and res:
            res = self.__field[y + 1][x].is_active
        return res

    def make_turn(self, colour):
        if self.__active_nodes[0].colour != colour:
            self.change_colour(colour)
            self.__set_new_active_nodes()
            self.__check_to_win()
            self.__turns_counter += 1
            return True
        return False

    def __check_to_win(self):
        if self.__cells_number == len(self.__active_nodes):
            self.__is_win = True

    def __initialize_field(self):
        self.__field = [
            [Node(Colours(random.randint(1, self.__colour_number)), x, y) for x in range(0, self.__field_size)] for y in
            range(0, self.__field_size)]
        self.__field[0][0].make_active()
        self.__active_nodes.append(self.__field[0][0])
        self.__new_active_nodes.append(self.__field[0][0])
        self.__set_new_active_nodes()

    def test_field(self):
        self.__field = [[Node(Colours(1), 0, 0), Node(Colours(2), 0, 1)],
                        [Node(Colours(2), 1, 0), Node(Colours(2), 1, 1)]]
        self.__active_nodes = []
        self.__active_nodes.append(self.__field[0][0])
        self.__field[0][0].make_active()

    def find_optimal_turns(self):
        a = 1
        b = 1
        c = -self.field_size ** 2 / self.coeff
        discriminant = b ** 2 - 4 * a * c
        if discriminant == 0:
            x = round(-b / (2 * a))
        else:
            x = round((-b + discriminant ** 0.5) / (2 * a))
        return x
