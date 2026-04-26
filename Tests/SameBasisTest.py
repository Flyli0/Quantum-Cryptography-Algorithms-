import random
import math
from BB84.RandomBit import random_bit
from QuantumSystemSimulation.Qubits import Basis, Qubits, State
from BB84.RandomBasis import rand_basis

alice_bits = []
alice_basis = []
alice_qubits = []

qubits_number = 100

for _ in range(qubits_number):
        # 1) Alice generates random bit sequence
        alice_bits.append(random_bit())
        # 2) Alice generates random basis sequence
        alice_basis.append(rand_basis())

    # 3) Alice encodes bits into qubits
for i in range(qubits_number):
        if alice_bits[i] == 0:
            if alice_basis[i] == Basis.RECTILINEAR:
                state = State.DEGREE0
                alice_qubits.append(Qubits(alice_basis[i], state))
            else:
                state = State.DEGREE45
                alice_qubits.append(Qubits(alice_basis[i], state))
        else:
            if alice_basis[i] == Basis.RECTILINEAR:
                state = State.DEGREE90
                alice_qubits.append(Qubits(alice_basis[i], state))
            else:
                state = State.DEGREE135
                alice_qubits.append(Qubits(alice_basis[i], state))
print(alice_bits)

# 4) Alice sends it to Bob
# Bob

bob_bits = []
bob_basis = alice_basis
# 5) Bob generates his random basis sequence
for _ in range(qubits_number):

        bob_bits.append(alice_qubits[_].measure(bob_basis[_]))

print(bob_bits)


# 6) Alice and Bob reveal their basis' to each other
# 7) Bob and Alic compare their basis and discard bits where basis didn't match
shifted_key_alice = ''
shifted_key_bob = ''
for i in range(qubits_number):
        if bob_basis[i] == alice_basis[i]:
            shifted_key_bob += str(bob_bits[i])
            shifted_key_alice += str(alice_bits[i])

    # 8) Error checking
k_size = len(shifted_key_alice)
checking_len = int(math.ceil(k_size*0.12))
if checking_len == 0:
        checking_len = 1
starting_point = random.randint(0,k_size-checking_len)
checking_part_bob = shifted_key_bob[starting_point:starting_point+checking_len]
checking_part_alice = shifted_key_alice[starting_point:starting_point + checking_len]
error_count = 0

for i in range(checking_len):
        if checking_part_bob[i] != checking_part_alice[i]:
            error_count += 1

final_key = ''
error_rate = error_count/checking_len * 100
print(f"ERROR RATE: {error_rate}")

if error_rate > 11:
        print("Evesdropper suspected, key discard")
else:
        final_key = shifted_key_bob[:starting_point] + shifted_key_bob[starting_point+checking_len:]
        print("KEY: " +  final_key)

# TEST
if len(final_key) == qubits_number-checking_len:
    print("100% bit agreement!")