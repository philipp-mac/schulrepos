import doctest
import abc
import coverage
import math

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
        '''
        >>> square = Square(5)
        >>> square.area()
        25
        '''
        return self.sidelen * self.sidelen

    def doubleSize(self):
        '''
        >>> square = Square(5)
        >>> square.area()
        25
        >>> square.doubleSize()
        >>> square.area()
        100
        '''
        self.sidelen *= 2


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        '''
        >>> circle = Circle(4)
        >>> int(circle.area())
        50
        '''
        return math.pi * ( self.radius * self.radius)

    def doubleSize(self):
        '''
        >>> circle = Circle(4)
        >>> int(circle.area())
        50
        >>> circle.doubleSize()
        >>> int(circle.area())
        201
        '''
        self.radius *= 2


doctest.testmod()