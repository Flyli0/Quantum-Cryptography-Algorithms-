import math
import random

class EntangledPair:
    def __init__(self):
        self.hidden_angle = random.uniform(0, math.pi)

    def measure_A(self, basis):
        return self._measure(basis, sign=1)

    def measure_B(self, basis):
        return self._measure(basis, sign=-1)  # ВАЖНО: анти-корреляция

    def _measure(self, basis, sign):
        angle = self._basis_to_angle(basis)

        p = 0.5 * (1 + math.cos(2 * (self.hidden_angle - angle)))

        return sign * (1 if random.random() < p else -1)

    def _basis_to_angle(self, basis):
        return {
            'a': 0,
            'a2': math.pi / 4,
            'b': math.pi / 8,
            'b2': 3 * math.pi / 8
        }[basis]