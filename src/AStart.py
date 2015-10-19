__author__ = 'Alex Black'

'''
This thing is crap right now, but it's pretty fun to mess with. I want to try to turn it into an a* implementation, but at this point
It just draws a grid and fills in random cells with red, which will be the walls at some point.

'''

import Tkinter as tk


class Demo(object):
    def __init__(self):
        # create the application
        self.width = 1000
        self.height = 1000
        self.col_spacing = 20
        self.row_spacing = 20
        root = self.init_main_app()
        self.init_canvis(root)

    def init_main_app(self):
        root = tk.Tk()
        root.geometry("1000x1000")
        root.title("A* demo")
        return root

    def init_canvis(self, root):
        self.canvas = tk.Canvas(root, height=self.height, width=self.width, bg="white")
        self.canvas.pack()
        self.setup_grid()
        root.mainloop()

    def setup_grid(self):
        for i in range(50):
            self.canvas.create_line(self.col_spacing * i, 0, self.col_spacing * i, self.width)
            self.canvas.create_line(0, self.row_spacing * i, self.height, self.row_spacing * i)


if __name__ == '__main__':
    demo = Demo()
