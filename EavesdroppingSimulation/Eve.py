import random
from QuantumSystemSimulation.Basis import Basis
from QuantumSystemSimulation.State import State
from QuantumSystemSimulation.Qubits import Qubits
from BB84 import rand_basis


class Eve:
    def __init__(self):
        self.intercepted_bits: list[int] = []
        self.basis_choices: list[Basis] = []
        self.basis_match_count: int = 0
        self.total_intercepted: int = 0

    def intercept(self, qubit: Qubits, alice_basis: Basis | None = None) -> Qubits:
        self.total_intercepted += 1

        eve_basis = rand_basis()
        self.basis_choices.append(eve_basis)

        measured_bit = qubit.measure(eve_basis)
        self.intercepted_bits.append(measured_bit)

        if alice_basis is not None and eve_basis == alice_basis:
            self.basis_match_count += 1

        if eve_basis == Basis.RECTILINEAR:
            state = State.DEGREE0 if measured_bit == 0 else State.DEGREE90
        else:
            state = State.DEGREE45 if measured_bit == 0 else State.DEGREE135

        return Qubits(eve_basis, state)

    def basis_match_rate(self) -> float:
        if self.total_intercepted == 0:
            return 0.0
        return self.basis_match_count / self.total_intercepted * 100

    def summary(self) -> dict:
        return {
            "total_intercepted": self.total_intercepted,
            "basis_match_rate_%": round(self.basis_match_rate(), 2),
        }