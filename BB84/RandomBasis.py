import random
from QuantumSystemSimulation.Basis import Basis


def rand_basis():  # returns random basis
    r = random.randint(0, 100)
    if r % 2 == 0:
        return Basis.DIAGONAL
    else:
        return Basis.RECTILINEAR
