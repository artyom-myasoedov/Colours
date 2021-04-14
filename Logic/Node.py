from Colours import Colours


class Node:

    def __init__(self, colour: Colours, x: int, y: int):
        self.__colour = colour
        self.__is_active = False
        self.__X = x
        self.__Y = y

    @property
    def is_active(self):
        return self.__is_active

    def make_active(self):
        self.__is_active = True

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour: Colours):
        self.__colour = colour

    @property
    def x(self):
        return self.__X

    @property
    def y(self):
        return self.__Y

    def __str__(self):
        return "x=" + str(self.__X) + " y=" + str(self.__Y) + " colour=" + str(self.__colour) + " is_active=" + str(
            self.__is_active)

    def __repr__(self):
        return self.__str__()
