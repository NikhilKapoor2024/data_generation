from random import choice

class RandomWalk:
    """A class representation of a random walk"""

    def __init__(self, num_points=500):
        """Initialize attributes"""
        self.num_points = num_points

        # All random walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
    

    def fill_walk(self):
        """Calculates the points in the walk"""
        
        # Keep taking steps until the walk reaches desired length
        while len(self.x_values) < self.num_points:
            # direction * distance = step
            x_dir = choice([1, -1])
            x_dist = choice([0, 1, 2, 3, 4])
            x_step = x_dir * x_dist

            y_dir = choice([1, -1])
            y_dist = choice([0, 1, 2, 3, 4])
            y_step = y_dir * y_dist

            # if the step goes nowhere, ignore and continue
            if x_step == 0 and y_step == 0:
                continue

            # calculate new positions and append
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)