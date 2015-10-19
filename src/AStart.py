__author__ = 'Alex Black'

from dependencies.graphics import *
import random

'''
This thing is crap right now, but it's pretty fun to mess with. I want to try to turn it into an a* implementation, but at this point
It just draws a grid and fills in random cells with red, which will be the walls at some point.

'''


class Demo(object):
    def __init__(self):

        self.width = 500
        self.height = 500
        self.gw = GraphWin("test", self.width, self.height)
        self.rows = 30
        self.cols = 30
        self.squairs = []
        self.setup_view()

    def setup_view(self):
        self.setup_grid()
        self.make_some_walls()
        self.draw_squairs()
        self.gw.getMouse()  # Pause to view result
        self.gw.close()

    def draw_squairs(self):
        for grid_item in self.squairs:
            if not grid_item.isWall:
                color = color_rgb(20, 20, 20)
                grid_item.setOutline(color)
                grid_item.draw(self.gw)

    def setup_grid(self):
        points = []

        x_vals = [x for x in range(-5, self.width, self.width / self.rows)]
        y_vals = [y for y in range(5, self.height, self.height / self.cols)]

        for index in range(0, self.rows):
            for sub_index in range(0, self.cols):
                if sub_index % 2:
                    if len(y_vals) > index + 1:
                        points.append(Point(x_vals[sub_index], y_vals[index + 1]))
                    else:
                        points.append(Point(x_vals[sub_index], y_vals[index]))
                else:
                    points.append(Point(x_vals[sub_index - 1], y_vals[index]))

                if len(points) > 1:
                    p2 = points.pop()
                    p1 = points.pop()
                    self.squairs.append(ExtendedRect(p1, p2))

    def make_some_walls(self):
        for i in range(0, len(self.squairs)/50):
            index = random.randint(0, len(self.squairs)-1)
            color = color_rgb(200, 0, 0)
            squere = self.squairs[index]
            squere.setFill(color)
            squere.draw(self.gw)


class ExtendedRect(object, Rectangle):
    def __init__(self, p1, p2):
        Rectangle.__init__(self, p1, p2)
        self.isWall = False


    def setFill(self, color):
        super(ExtendedRect, self).setFill(color)
        self.isWall = True
        # super.setFill(color)



if __name__ == '__main__':
    demo = Demo()
