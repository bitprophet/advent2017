from advent.day3 import spiral_steps, build_grid


personal_input = 347991


class build_grid_:
    def example(self):
        assert build_grid(including=23) == [
            17, 16, 15, 14, 13,
            18, 5,  4,  3,  12,
            19, 6,  1,  2,  11,
            20, 7,  8,  9,  10,
            21, 22, 23, 24, 25,
        ]


class spiral_steps_:
    def base(self):
        assert spiral_steps(square=1) == 0

    def near(self):
        assert spiral_steps(square=12) == 3

    def nearish(self):
        assert spiral_steps(square=23) == 2

    def far(self):
        assert spiral_steps(square=1024) == 31

    def solution(self):
        assert spiral_steps(square=personal_input) == "???"
