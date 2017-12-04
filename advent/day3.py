from itertools import chain, cycle
from math import ceil, sqrt

from tabulate import tabulate


# Constants because LOL
Spiral = Left, Up, Right, Down = tuple(object() for _ in range(4))


class Grid:
    def __init__(self, including):
        self.including = including
        # A grid that includes given number must be NxN where N is the square
        # root of the number, rounded up.
        self.side = ceil(sqrt(self.including))
        self.end = self.side * self.side
        print("Side length: {} (end: {})".format(self.side, self.end))
        # Initialize such an array.
        self.grid = [
            [None for y in range(self.side)]
            for x in range(self.side)
        ]
        print("Empty:")
        self.display()
        # Other bookkeeping
        self.spiraling = cycle(Spiral)

    def display(self):
        print(tabulate(self.grid, tablefmt='grid'))

    def fill(self):
        # Walk the spiral backwards, filling in from bottom right. Easier than
        # the other way 'round!
        self.x = self.y = self.side - 1
        current = self.end
        self.grid[self.y][self.x] = current
        print("Initialized:")
        self.display()
        self.heading = next(self.spiraling)
        while current > 1:
            self.move()
            current -= 1
            self.write(current)
        print("Filled:")
        self.display()

    def write(self, number):
        print("Writing value {} to ({}, {})".format(number, self.x, self.y))
        self.grid[self.y][self.x] = number

    def is_empty(self, x, y):
        try:
            return self.grid[y][x] is None
        except IndexError: # implies x or y was < 0
            # TODO: this doesn't quite fit the question of "is empty", so
            # either rename the method (lol) or rethink
            return False

    def turn(self):
        self.heading = next(self.spiraling)

    def move(self):
        # Pretend to move ahead along heading
        new_x, new_y = self.x, self.y
        print("Moving: starting at ({}, {})".format(new_x, new_y))
        if self.heading is Left:
            print("Heading: Left")
            new_x -= 1
        elif self.heading is Up:
            print("Heading: Up")
            new_y -= 1
        elif self.heading is Right:
            print("Heading: Right")
            new_x += 1
        elif self.heading is Down:
            print("Heading: Down")
            new_y += 1
        print("Would move to: ({}, {})".format(new_x, new_y))
        # If the next cell in this heading wouldn't be valid, spiral & try
        # moving again, without actually updating coords.
        if not self.is_empty(new_x, new_y):
            print("That cell isn't empty/valid, turning!")
            self.turn()
            return self.move()
        # Otherwise, must be safe to move, so punch in those coords.
        print("Looks good! Moving to ({}, {})".format(new_x, new_y))
        self.x = new_x
        self.y = new_y

    def steps_to_center(self):
        pass


def spiral_steps(square):
    return Grid(including=square).steps_to_center()
