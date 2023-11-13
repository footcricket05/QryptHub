#!/usr/bin/env python
# coding: utf-8

# # Implementation of BB84 protocol using a Quantum Key Distribution (QKD) setup

# In[1]:


from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import random


# In[2]:


# Function to create a random bitstring of a given length
def generate_bitstring(length):
    return ''.join([random.choice(['0', '1']) for _ in range(length)])


# In[3]:


# Function to encode bits on qubits based on chosen bases
def encode_bits(qc, bits, bases):
    for i in range(len(bits)):
        if bases[i] == 0:  # Rectilinear basis
            if bits[i] == '1':
                qc.x(i)
        elif bases[i] == 1:  # Diagonal basis
            if bits[i] == '0':
                qc.h(i)
            else:
                qc.x(i)
                qc.h(i)


# In[4]:


# Function to measure qubits based on chosen bases
def measure_bits(qc, bases):
    measurements = []
    for i in range(len(bases)):
        if bases[i] == 0:  # Rectilinear basis
            qc.measure(i, i)
        elif bases[i] == 1:  # Diagonal basis
            qc.h(i)
            qc.measure(i, i)
            qc.h(i)
        measurements.append(i)
    return measurements


# In[5]:


# Function to perform error checking
def error_check(alice_bitstring, sifted_key, measurements):
    errors = 0
    for i in measurements:
        if sifted_key[i] != int(alice_bitstring[i]):
            errors += 1
    return errors


# In[6]:


# Function for privacy amplification
def privacy_amplification(sifted_key):
    # Perform a simple hash function (e.g., XOR) for privacy amplification
    hashed_key = [str(int(sifted_key[i]) ^ int(sifted_key[i + 1])) for i in range(0, len(sifted_key) - 1, 2)]
    return ''.join(hashed_key)


# In[7]:


# Simulate the QKD setup with error checking and privacy amplification
def qkd_setup_with_error_privacy():
    # Alice generates a random bitstring and bases
    alice_bitstring = generate_bitstring(4)
    alice_bases = [random.randint(0, 1) for _ in range(4)]

    # Bob chooses random bases
    bob_bases = [random.randint(0, 1) for _ in range(4)]

    # Set up the quantum circuit
    qc = QuantumCircuit(4, 4)

    # Alice encodes her bits on qubits
    encode_bits(qc, alice_bitstring, alice_bases)

    # Bob measures the qubits based on his chosen bases
    bob_measurements = measure_bits(qc, bob_bases)

    # Simulate the quantum communication channel (idealized)
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1)
    result = job.result()
    counts = result.get_counts()

    # Bob and Alice compare bases to filter bits
    sifted_key = [int(counts.get(bin(i)[2:].zfill(4), 0)) % 2 for i in range(16)]

    # Error checking
    errors = error_check(alice_bitstring, sifted_key, bob_measurements)

    # Privacy amplification
    final_key = privacy_amplification(sifted_key)

    return alice_bitstring, bob_measurements, sifted_key, counts, errors, final_key


# In[8]:


# Run the QKD setup with error checking and privacy amplification
alice_bits, bob_measurements, sifted_key, counts, errors, final_key = qkd_setup_with_error_privacy()


# In[9]:


# Display results
print("Alice's random bitstring:", alice_bits)
print("Bob's measurements:", bob_measurements)
print("Sifted key:", sifted_key)
print("Measurement Results:", counts)
print("Errors:", errors)
print("Final Key (after privacy amplification):", final_key)


# In[ ]:




