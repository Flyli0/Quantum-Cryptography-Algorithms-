from Basis import Basis
from State import State
# Qubits behaviour simulation


class Qubits:  # basis and its state = cubits
    basis: Basis
    state: State

    def __init__(self, basis: Basis, state: State):  # cubit initialization
        self.basis = basis
        if self.basis in [Basis.DIAGONAL] and state in [State.DEGREE45, State.DEGREE135]:
            self.state = state
        elif self.basis in [Basis.RECTILINEAR] and state in [State.DEGREE0, State.DEGREE90]:
            self.state = state

    def measure_basis(self, try_basis: Basis):  # basis measurement simulation
        if self.basis == try_basis:
            return True
        else:  # if measurement is wrong Qubit collapses
            self.basis = Basis.WHATISTHAT
            self.state = State.DEGREEWTF

    def measure_state(self, try_state: State):  # state measurement simulation
        if self.state == State:
            return True
        else:  # if measurement is wrong Qbit collapses
            self.state = State.DEGREEWTF
            self.basis = Basis.WHATISTHAT


