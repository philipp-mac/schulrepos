import abc
import math
import coverage
import pytest

class Figure(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def area(self):
        pass
    
    @abc.abstractmethod
    def doubleSize(self):
        pass

class Square(Figure):
    def __init__(self, sidelen):
        super().__init__()
        self.sidelen = sidelen

    def area(self):
        return self.sidelen * self.sidelen

    def doubleSize(self):
        self.sidelen *= 2


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * ( self.radius * self.radius)

    def doubleSize(self):
        self.radius *= 2