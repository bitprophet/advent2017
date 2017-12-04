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
        # Initialize such an array.
        self.grid = [
            [None for y in range(self.side)]
            for x in range(self.side)
        ]
        # Other bookkeeping
        self.spiraling = cycle(Spiral)
        # Identify where the center is; the spiral-drawing algo doesn't
        # currently need it (tho if it changed to be in->out, it would) but
        # steps-to-center computation does.
        self.halfway = self.side // 2

    def display(self):
        print(tabulate(self.grid, tablefmt='grid'))

    def walk(self):
        # Walk the spiral backwards from bottom right. Easier than the other
        # way 'round!
        self.x = self.y = self.side - 1
        self.heading = next(self.spiraling)
        while self.x != self.halfway or self.y != self.halfway:
            yield self.x, self.y
            self.move()
            self.display()

    def fill(self):
        current = self.end
        for x, y in self.walk():
            self.write(current)
            current -= 1
        self.write(current)

    def write(self, number):
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
        if self.heading is Left:
            new_x -= 1
        elif self.heading is Up:
            new_y -= 1
        elif self.heading is Right:
            new_x += 1
        elif self.heading is Down:
            new_y += 1
        # If the next cell in this heading wouldn't be valid, spiral & try
        # moving again, without actually updating coords.
        if not self.is_empty(new_x, new_y):
            self.turn()
            return self.move()
        # Otherwise, must be safe to move, so punch in those coords.
        self.x = new_x
        self.y = new_y

    def steps_to_center(self):
        # TODO: eureka! could simply cut out some of fill() - as soon as we
        # write(number==self.including) we are capable of answering this
        # particular question about the grid!

        # 'Move' the coords to the actual number in question (self.including)
        # Then simply get the absolute difference between those coords and
        # self.halfway, and sum them.
        pass


def spiral_steps(square):
    return Grid(including=square).steps_to_center()
