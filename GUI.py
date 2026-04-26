import tkinter as tk
import random

from BB84.RandomBit import random_bit
from BB84.RandomBasis import rand_basis
from QuantumSystemSimulation.Qubits import Qubits, Basis, State


class BB84Sim:
    def __init__(self, n, eve_enabled, noise):
        self.n = n
        self.eve_enabled = eve_enabled
        self.noise = noise

        self.index = 0

        self.alice_bits = []
        self.alice_basis = []
        self.bob_bits = []
        self.bob_basis = []

        self.sift_a = []
        self.sift_b = []

    def step(self):
        if self.index >= self.n:
            return None

        a_bit = random_bit()
        a_basis = rand_basis()

        if a_bit == 0:
            state = State.DEGREE0 if a_basis == Basis.RECTILINEAR else State.DEGREE45
        else:
            state = State.DEGREE90 if a_basis == Basis.RECTILINEAR else State.DEGREE135

        qubit = Qubits(a_basis, state)

        if self.eve_enabled:
            eve_basis = rand_basis()
            measured = qubit.measure(eve_basis)

            if eve_basis == Basis.RECTILINEAR:
                state = State.DEGREE0 if measured == 0 else State.DEGREE90
            else:
                state = State.DEGREE45 if measured == 0 else State.DEGREE135

            qubit = Qubits(eve_basis, state)

        b_basis = rand_basis()
        b_bit = qubit.measure(b_basis)

        if random.random() < self.noise:
            b_bit = 1 - b_bit

        self.alice_bits.append(a_bit)
        self.alice_basis.append(a_basis)
        self.bob_bits.append(b_bit)
        self.bob_basis.append(b_basis)

        if a_basis == b_basis:
            self.sift_a.append(a_bit)
            self.sift_b.append(b_bit)

        self.index += 1

        return True

    def stats(self, error_threshold):
        if len(self.sift_a) == 0:
            return {
                "total": self.n,
                "sifted": 0,
                "errors": 0,
                "error_rate": 0,
                "secure": False,
                "key": "",
                "basis_match_rate": 0,
                "sample_size": 0,
                "efficiency": 0
            }

        sample = max(1, int(len(self.sift_a) * 0.1))
        start = random.randint(0, max(0, len(self.sift_a) - sample))

        errors = 0
        for i in range(sample):
            if self.sift_a[start + i] != self.sift_b[start + i]:
                errors += 1

        error_rate = (errors / sample) * 100

        basis_match_rate = (len(self.sift_a) / self.n) * 100

        final_key_len = min(256, len(self.sift_a))
        efficiency = (final_key_len / self.n) * 100

        return {
            "total": self.n,
            "sifted": len(self.sift_a),
            "errors": errors,
            "error_rate": error_rate,
            "secure": error_rate < error_threshold * 100,
            "key": "".join(map(str, self.sift_a[:256])),
            "basis_match_rate": basis_match_rate,
            "sample_size": sample,
            "final_key_length": final_key_len,
            "efficiency": efficiency
        }


class BB84GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BB84 Simulator")
        self.root.geometry("750x600")

        self.sim = None

        self.n_var = tk.StringVar(value="1000")
        self.eve_var = tk.BooleanVar()
        self.noise_var = tk.DoubleVar(value=0.0)
        self.threshold_var = tk.DoubleVar(value=0.11)

        self.build_ui()

    def build_ui(self):
        frm = tk.Frame(self.root)
        frm.pack()

        tk.Label(frm, text="Photons").grid(row=0, column=0)
        tk.Entry(frm, textvariable=self.n_var).grid(row=0, column=1)

        tk.Checkbutton(frm, text="Eve enabled", variable=self.eve_var).grid(row=1, column=0)

        tk.Label(frm, text="Noise (0–0.05)").grid(row=2, column=0)
        tk.Entry(frm, textvariable=self.noise_var).grid(row=2, column=1)

        tk.Label(frm, text="Error threshold").grid(row=3, column=0)
        tk.Entry(frm, textvariable=self.threshold_var).grid(row=3, column=1)

        tk.Button(frm, text="Start", command=self.start).grid(row=4, column=0)

        self.output = tk.Text(self.root, height=25)
        self.output.pack()

    def start(self):
        n = int(self.n_var.get())
        self.sim = BB84Sim(n, self.eve_var.get(), self.noise_var.get())

        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "Simulation running...\n")

        while self.sim.step():
            pass

        stats = self.sim.stats(self.threshold_var.get())

        self.output.insert(tk.END, "\n=== FINAL ===\n")

        self.output.insert(tk.END, f"Total photons: {stats['total']}\n")
        self.output.insert(tk.END, f"Sifted key length: {stats['sifted']}\n")

        self.output.insert(tk.END, f"Basis match rate: {stats['basis_match_rate']:.2f}%\n")
        self.output.insert(tk.END, f"Bits used for error checking: {stats['sample_size']}\n")
        self.output.insert(tk.END, f"Errors: {stats['errors']}\n")
        self.output.insert(tk.END, f"Error rate: {stats['error_rate']:.2f}%\n")

        self.output.insert(tk.END, f"Final key length: {stats['final_key_length']}\n")
        self.output.insert(tk.END, f"Efficiency: {stats['efficiency']:.2f}%\n")

        self.output.insert(tk.END, f"Secure: {stats['secure']}\n")
        self.output.insert(tk.END, f"Key ({stats['final_key_length']}): {stats['key']}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = BB84GUI(root)
    root.mainloop()