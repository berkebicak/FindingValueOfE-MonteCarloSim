import random
from numba import jit

class findingValueOfE:

    def __init__(self):
        self.av = 0
        self.n = 0

    def get_e(self):
        return self.av / self.n

    def value_of_e(self, nn):
        (self.av, self.n) = self.value_of_e_static(nn)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def value_of_e_static(nn):
        av = 0
        for _ in range(nn):
            S = 0
            x = 0
            while S < 1:
                S += random.uniform(0, 1)
                x += 1
            av += x
        return av, nn
