from Basis import Basis
from State import State
import random
# Qubits behaviour simulation


class Qubits:  # basis and its state = cubits
    def __init__(self, basis: Basis, state: int):  # cubit initialization
        self.basis = basis
        if state not in [0,1]:
            raise AttributeError
        else:
            self.state = state

    def measure(self, try_basis: Basis) -> int:  # basis measurement simulation
        if self.basis == try_basis:
            return self.state
        else:  # if measurement is wrong Qubit collapses
            self.basis = Basis.WHATISTHAT
            self.state = random.randint(0,1)
            return self.state



