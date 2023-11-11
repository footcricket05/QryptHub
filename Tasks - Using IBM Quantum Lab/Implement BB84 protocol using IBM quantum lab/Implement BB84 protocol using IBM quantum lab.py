#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import random


# In[2]:


# Define the bitstring variable
bitstring = '1010'


# In[3]:


# Set up the quantum circuit with two qubits and two classical bits
qc = QuantumCircuit(2, 2)


# In[4]:


# Alice generates a random bit string and encodes it onto the qubits using one of four possible bases
# For example, to encode the first bit in the rectilinear basis, Alice applies an X gate to the first qubit
for i in range(2):
    if bitstring[i] == '1':
        qc.x(i)


# In[5]:


# Bob randomly chooses a basis for each qubit and measures them
# For example, to measure the first qubit in the rectilinear basis, Bob applies an H gate to the first qubit and measures both qubits
basis = [random.randint(0, 1) for _ in range(2)]
for i in range(2):
    if basis[i] == 1:
        qc.h(i)

qc.measure([0, 1], [0, 1])


# In[6]:


# Alice and Bob publicly compare which bases they used for each qubit
# If they used the same basis, they keep the corresponding bit. Otherwise, they discard it
for i in range(2):
    if basis[i] == 1:
        qc.measure(i, i)
    else:
        qc.h(i)
        qc.measure(i, i)


# In[7]:


# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1)
result = job.result()
counts = result.get_counts()


# In[8]:


# Extract the measurement results
alice_basis = [int(b) for b in bitstring]
alice_result = [int(b) for b in bitstring]

for i in range(2):
    if basis[i] == 0:
        alice_result[i] = -1  # Placeholder for bits discarded due to mismatched bases


# In[9]:


# Visualize the measurement results
print("Measurement Results:", counts)


# In[10]:


# Display the results
print("Alice's generated bitstring:", bitstring)
print("Alice's chosen bases:", alice_basis)
print("Bob's chosen bases:", basis)
print("Bob's measurement results:", [int(k) for k in counts.keys()][0])


# In[11]:


# Verify if Alice's and Bob's bases match
matching_bases = sum(1 for i in range(2) if alice_basis[i] == basis[i])
print("Matching bases:", matching_bases)


# In[12]:


# Calculate the percentage of matching bits
matching_bits = sum(1 for i in range(2) if alice_result[i] == int(bitstring[i]))
percentage_matching = (matching_bits / matching_bases) * 100
print("Percentage of matching key bits:", percentage_matching)


# In[ ]:




