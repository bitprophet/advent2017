from math import ceil, sqrt
from pprint import pprint
from itertools import chain


# Constants because LOL
Right, Up, Left, Down = range(4)


def print_grid(grid):
    lengths = [len(str(x)) for x in chain.from_iterable(grid)]
    width = max(lengths)
    padded = [
        [("{:>{width}}" if x else "{}").format(x, width=width) for x in y]
        for y in grid
    ]
    pprint(padded)


def build_grid(including):
    # A grid that includes given number must be NxN where N is the square root
    # of the number, rounded up.
    side = ceil(sqrt(including))
    end = side * side
    print("Side length: {} (end: {})".format(side, end))
    # Initialize such an array.
    grid = [[None for y in range(side)] for x in range(side)]
    print_grid(grid)
    # Given that math, we know the side will always be an odd number, so we can
    # divide by 2 and floor that to get the (X and/or Y) index of the start
    # point. (This doesn't work perfectly at small or uneven sizes, but for
    # now, we don't need it to?)
    start_index = side // 2
    print(start_index)
    # Now we can walk the spiral, starting at the center, going right
    x = y = start_index
    heading = Right
    for number in range(1, end + 1):
        # Start by assuming pointer's been moved, and fill in. (remember how 2D
        # arrays work - greater dimensions first.)
        grid[y][x] = number
    print_grid(grid)


def spiral_steps(square):
    pass
