from advent.day1 import captcha

class captcha_:
    def simple(self):
        assert captcha("1122") == 3

    def all_same(self):
        assert captcha("1111") == 4

    def all_different(self):
        assert captcha("1234") == 0

    def circular(self):
        assert captcha("91212129") == 9
