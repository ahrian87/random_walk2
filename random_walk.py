from random import choice


class RandomWalk():
    """"Class for generating random walk"""

    def __init__(self, num_points=5000):
        """Random attributes initialization"""
        self.num_points = num_points

        # Starting point is (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Generating all points for random walk"""
        # Making steps till expected number of points
        while len(self.x_values) < self.num_points:

            # Choosing the direction and distance to walk
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            # Establishing next X and Y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)