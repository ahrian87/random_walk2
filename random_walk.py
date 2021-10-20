from random import choice

class RandomWalk():
    """"Class for generating random walk"""

    def __init__(self, num_points=5000):
        """Random attributes initialization"""
        self.num_points = num_points

        # Starting point is (0,0)
        self.x_values = [0]
        self.y_values = [0]