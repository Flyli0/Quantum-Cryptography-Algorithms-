from E91.Entaglement import EntangledPair
from EavesdroppingSimulation.E91Eve import EveE91
from E91.RandomBasis import rand_basis_a, rand_basis_b
from E91.CHSH import chsh

def e91(measurement_number, is_eve: bool):
    entangled_pairs: [EntangledPair()] = []
    # random Source creates entangled pairs
    for i in range(measurement_number):
        entangled_pairs.append(EntangledPair())

    #Eve if exists measures
    if is_eve:
        eve_pair = []
        eve = EveE91()
        for p in entangled_pairs:
            ep = eve.intercept(p)
            eve_pair.append(ep)
        entangled_pairs = eve_pair

    #Alice
    alice_bases = []
    bob_bases = []
    measurements = {
        ('a', 'b'): [],
        ('a', 'b2'): [],
        ('a2', 'b'): [],
        ('a2', 'b2'): []
    }
    for i in range(measurement_number):  # Alice and Bob's actions
        alice_basis = rand_basis_a()  # Alice generates random Basis sequence
        bob_basis = rand_basis_b()  # Bob too
        alice_bit = entangled_pairs[i].measure_A(alice_basis)  # Alice and Bob measure qubits with their bases
        bob_bit = entangled_pairs[i].measure_B(bob_basis)
        measurements[(alice_basis,bob_basis)].append((alice_bit,bob_bit))  # record it into measurements
        alice_bases.append(alice_basis)
        bob_bases.append(bob_basis)

    s = chsh(measurements)  # count entanglement consequences
    print(f"Bell-CHSH: {s}")
    if s > -0.2:
        print("All good")
    else:
        print("Evesdropper detected")  # Checking of an eavesdropper

