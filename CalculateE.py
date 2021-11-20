import random

class findingValueOfE:

    def __init__(self):
        self.av = 0
        self.n = 0

    def get_e(self):
        return self.av / self.n

    def value_of_e(self, nn):
        av = 0
        for _ in range(nn):
            S = 0
            x = 0
            while S < 1:
                S += random.uniform(0, 1)
                x += 1
            av += x
        self.n = nn
        self.av = av
