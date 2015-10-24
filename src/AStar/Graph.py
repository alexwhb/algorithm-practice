__author__ = 'Winston'


class Graph(object):
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]
