from advent.day3 import spiral_steps


personal_input = 347991


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
