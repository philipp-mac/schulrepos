import figures
import pytest as pytest
import coverage

def CircleTest():
    circle = figures.Circle(4)
    assert int(circle.area()) == 50
    circle.doubleSize()
    assert circle.radius == 8
    assert int(circle.area()) == 201

    del circle
    with pytest.raises(Exception):
        circle = figures.Circle("test")
        circle.area()

def SquareTest():
    square = figures.Square(5)
    assert square.area() == 25
    square.doubleSize()
    assert square.sidelen == 10
    assert square.area() == 100

    del square
    with pytest.raises(Exception):
        square = figures.Circle("test")
        square.area()
       
SquareTest()
CircleTest()