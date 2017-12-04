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
        # Initialize spiraling here to proof against being walk()'d multiple
        # times - the end direction will not necessarily match the start
        # direction!
        self.spiraling = cycle(Spiral)
        self.heading = next(self.spiraling)
        while self.x != self.halfway or self.y != self.halfway:
            yield self.x, self.y
            self.move()

    def fill(self):
        current = self.end
        for x, y in self.walk():
            self.write(current)
            current -= 1
        self.write(current)

    def write(self, number):
        self.grid[self.y][self.x] = number

    def read(self):
        return self.grid[self.y][self.x]

    def should_turn(self, x, y):
        try:
            lookahead = self.grid[y][x]
            if lookahead is None:
                # If next cell exists & is None, keep going, we're in a fill
                # action presumably and it can be filled next.
                return False
            else:
                # Non-None (and clearly not an IndexError) means it's some
                # already-filled number, and we can tell whether to spiral
                # inwards if the 'next' number in this direction is larger than
                # the one currently pointed to (presuming we are walking
                # largest->smallest.)
                next_bigger = lookahead > self.read()
                return next_bigger
        except IndexError: # implies x or y was < 0
            return True

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
        if self.should_turn(new_x, new_y):
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
        for x, y in self.walk():
            value = self.read()
            print("Walking: ({}, {}) -> {}".format(x, y, value))
            if value is self.including:
                break
        self.display()
        print("({}, {})".format(x, y))
        # Then simply get the absolute difference between those coords and
        # self.halfway, and sum them.
        return abs(x - self.halfway) + abs(y - self.halfway)


def spiral_steps(square):
    grid = Grid(including=square)
    grid.fill()
    return grid.steps_to_center()
