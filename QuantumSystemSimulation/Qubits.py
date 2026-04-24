from Basis import Basis
from State import State
import random
# Qubits behaviour simulation


class Qubits:  # basis and its state = cubits
    def __init__(self, basis: Basis, state: State):  # cubit initialization
        self.basis = basis
        self.state = State.RANDOMSTATE
        if self.basis in [Basis.DIAGONAL] and state in [State.DEGREE45, State.DEGREE135]:
            self.state = state
        elif self.basis in [Basis.RECTILINEAR] and state in [State.DEGREE0, State.DEGREE90]:
            self.state = state
        else:
            raise AttributeError

    def measure(self, try_basis: Basis) -> int:  # basis measurement simulation
        if self.basis == try_basis:
            return self.state.value
        else:  # if measurement is wrong Qubit collapses
            self.basis = Basis.WHATISTHAT
            self.state = State.RANDOMSTATE
            return self.state.value



