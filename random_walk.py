from random import choice


class RandomWalk():
    """"Class for generating random walk"""

    def __init__(self, num_points=5000):
        """Random attributes initialization"""
        self.num_points = num_points

        # Starting point is (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        # Choosing the direction and distance to walk
        step_direction = choice([1, -1])
        step_distance = choice([0, 1, 2, 3, 4])
        return step_direction * step_distance


    def fill_walk(self):
        """Generating all points for random walk"""
        # Making steps until reaching expected number of points
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # Establishing next X and Y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
