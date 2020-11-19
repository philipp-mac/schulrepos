import figures
import unittest
import coverage

class SquareTest(unittest.TestCase):
    def setUp(self):
        self.square = figures.Square(4)

    def testArea(self):
        self.assertEquals(self.square.area(), 16)

    def testDoubleSize(self):
        self.square.doubleSize()
        self.assertTrue(self.square.sidelen == 8)
        self.assertEquals(self.square.area() == 64)

class CircleTest(unittest.TestCase):
    def setUp(self):
        self.circle = figures.Circle(4)

    def testArea(self):
        assert int(self.circle.area()) == 50

    def testDoubleSize(self):
        self.circle.doubleSize()
        assert self.circle.radius == 8
        assert int(self.circle.area()) == 201