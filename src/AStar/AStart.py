__author__ = 'Winston'


from Queue import Queue


# class AStar(object):
#     def __init__(self):
#         pass

# http://www.redblobgames.com/pathfinding/a-star/implementation.html
def breadth_first_search(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {start: True}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        print("Visiting %r" % current)
        for next_el in graph.neighbors(current):
            if next_el not in came_from:
                frontier.put(next_el)
                came_from[next_el] = True

    return came_from

if __name__ == '__main__':
    pass