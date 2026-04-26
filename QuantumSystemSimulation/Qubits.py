from QuantumSystemSimulation.Basis import Basis
from QuantumSystemSimulation.State import State
import random
# Qubits behaviour simulation

class Qubits:
    def __init__(self, basis: Basis, state: State):
        self.basis = basis

        if self.basis == Basis.DIAGONAL and state in [State.DEGREE45, State.DEGREE135]:
            self.state = state
        elif self.basis == Basis.RECTILINEAR and state in [State.DEGREE0, State.DEGREE90]:
            self.state = state
        else:
            raise AttributeError("Invalid basis-state combination")

        self.bit = State.state_to_bit(state)

    def measure(self, try_basis: Basis) -> int:
        if self.basis == try_basis:
            return self.bit
        else:
            return random.randint(0, 1)


