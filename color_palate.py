import random


class RandomColor():
    def __init__(self):
        pass

    @staticmethod
    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        r_color = (r, g, b)
        return r_color
