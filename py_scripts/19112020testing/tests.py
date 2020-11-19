import figures
import pytest


def SquareTest():
    square = figures.Square(4)
    assert square.area() == 16

def CircleTest():
    circle = figures.Circle(4)
    assert int(circle.area()) == 50
    del circle
    with pytest.raises(Exception):
        circle = figures.Circle("test")
        circle.area()



    

    
SquareTest()
CircleTest()