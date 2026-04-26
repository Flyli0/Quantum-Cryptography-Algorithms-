import math
import random


class EntangledPair:  # simulation of an entangled qubits
    def __init__(self):
        self.hidden_angle = random.uniform(0, math.pi)  # this hidden angle will ensure some connection -> correlation between qubits

    def measure_A(self, basis):  # measurement that Alice conducts
        return self._measure(basis, sign=1)

    def measure_B(self, basis):
        return self._measure(basis, sign=-1)   # measurement that Bob conducts with negative correlation

    def _measure(self, basis, sign):  # main measurement function changes correlation by changing p
        angle = self._basis_to_angle(basis)

        p = 0.5 * (1 + math.cos(2 * (self.hidden_angle - angle)))

        return sign * (1 if random.random() < p else -1)

    def _basis_to_angle(self, basis):  # just function to transform bases into corresponding angles
        return {
            'a': 0,
            'a2': math.pi / 4,
            'b': math.pi / 8,
            'b2': 3 * math.pi / 8
        }[basis]