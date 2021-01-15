import random

import numpy as np
import matplotlib.pyplot as plt

class MazeNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.visited = False
        self.fruitful = True
        self.previous = None
        self.must_be_wall = False
        self.distance = 0

    def __hash__(self):
        ### Unique as long as the maze doesn't have rows 10^6 long.
        return 1000000*self.x + self.y

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_valid_neighbors(self):
        ### Return a list of the neighboring nodes that could be visited
        ### next. Also, mark this cell as not fruitful if it has no valid
        ### neighbors.
        valid_neighbors = []
        for n in self.neighbors:
            if n.visited:
                continue
            num_visited_neighbors = 0
            for nn in n.neighbors:
                if nn.visited:
                    num_visited_neighbors += 1
            if num_visited_neighbors < 2:
                valid_neighbors.append(n)

        if not valid_neighbors:
            self.fruitful = False
        
        return valid_neighbors

    def visit(self):
        self.visited = True

    def visit_from(self, previous):
        self.visited = True
        self.previous = previous
        self.distance = previous.distance + 1


def gen_grid(height, width, strategy = 'random_leaf'):
    ### First, create the grid of MazeNode objects.
    node_grid = []

    for i in range(height):
        node_grid.append([])
        for j in range(width):
            node = MazeNode(i, j)
            node_grid[i].append(node)
            if i > 0:
                node_grid[i - 1][j].add_neighbor(node)
                node.add_neighbor(node_grid[i - 1][j])
            if j > 0:
                node_grid[i][j - 1].add_neighbor(node)
                node.add_neighbor(node_grid[i][j - 1])

    ### Second, decide which nodes are walls and which are free.
    if strategy == 'depth_first':
        current = node_grid[0][0]
        current.visit()
        current.distance = 0

        farthest_node = current

        while current is not None:
            valid_neighbors = current.get_valid_neighbors()
            if not valid_neighbors:
                current = current.previous
            else:
                next_node = random.choice(valid_neighbors)
                next_node.visit()
                next_node.previous = current
                next_node.distance = current.distance + 1
                current = next_node

            if current is not None:
                if current.distance > farthest_node.distance:
                    farthest_node = current

    elif strategy == 'random_leaf':
        current = node_grid[0][0]
        current.visit()
        current.distance = 0

        leaves = set([current])

        farthest_node = current

        while leaves:
            to_expand = random.choice(list(leaves))
            valid_neighbors = to_expand.get_valid_neighbors()
            if not valid_neighbors:
                leaves.remove(to_expand)
            else:
                next_node = random.choice(valid_neighbors)
                next_node.visit_from(to_expand)
                leaves.add(next_node)
                if next_node.distance > farthest_node.distance:
                    farthest_node = next_node

    ### And finally convert it back to a list of lists.
    grid = [[0 for j in range(width)] for i in range(height)]

    for i in range(height):
        for j in range(width):
            if not node_grid[i][j].visited:
                grid[i][j] = 1

    print(np.array(grid))
    return grid

if __name__ == '__main__':
    m = gen_grid(30, 40)
    plt.matshow(m)
    plt.show()
