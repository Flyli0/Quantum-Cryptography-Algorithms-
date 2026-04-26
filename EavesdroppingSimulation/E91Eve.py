import random
import math
import math
from E91.Entaglement import EntangledPair
from EavesdroppingSimulation.ClassicalPair import ClassicalPair


class EveE91:
    def intercept(self, pair):
        basis = random.choice(['a','a2','b','b2'])

        a = pair.measure_A(basis)
        b = pair.measure_B(basis)

        new_pair = ClassicalPair(a,b)


        return new_pair