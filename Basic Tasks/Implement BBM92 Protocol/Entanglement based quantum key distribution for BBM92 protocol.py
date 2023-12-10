#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram


# In[2]:


def create_entangled_state(qc, alice_qubit, bob_qubit):
    """Create an entangled Bell state."""
    qc.h(alice_qubit)
    qc.cx(alice_qubit, bob_qubit)


# In[3]:


def alice_operations(qc, alice_qubit, ancilla_qubit):
    """Alice's operations in the BBM92 protocol."""
    qc.h(alice_qubit)
    qc.cx(alice_qubit, ancilla_qubit)
    qc.measure(alice_qubit, 0)
    qc.measure(ancilla_qubit, 1)


# In[4]:


def bob_operations(qc, alice_qubit, bob_qubit, ancilla_qubit):
    """Bob's operations in the BBM92 protocol."""
    qc.cx(alice_qubit, bob_qubit)
    qc.h(alice_qubit)
    qc.measure(alice_qubit, 2)
    qc.measure(bob_qubit, 3)


# In[5]:


def error_correction(qc, alice_qubit, ancilla_qubit):
    """Error correction using the three-qubit bit flip code."""
    qc.cx(alice_qubit, ancilla_qubit)
    qc.cz(ancilla_qubit, 1)
    qc.cx(alice_qubit, ancilla_qubit)


# In[6]:


def privacy_amplification(qc, alice_qubit, bob_qubit):
    """Privacy amplification by XORing the remaining qubits."""
    qc.cx(alice_qubit, bob_qubit)


# In[7]:


# Define the quantum circuit
qc = QuantumCircuit(4, 4)


# In[8]:


# Create an entangled state (Bell state)
create_entangled_state(qc, 0, 2)


# In[9]:


# Alice's operations
alice_operations(qc, 0, 1)


# In[10]:


# Bob's operations
bob_operations(qc, 0, 2, 3)


# In[11]:


# Error correction
error_correction(qc, 1, 2)


# In[12]:


# Privacy amplification
privacy_amplification(qc, 0, 2)


# In[13]:


# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1)
result = job.result()
counts = result.get_counts()


# In[14]:


# Display the results
print("Measurement Results:")
print(counts)


# In[15]:


# Extract the final key bits
alice_key = int(list(counts.keys())[0][:2], 2)
bob_key = int(list(counts.keys())[0][2:], 2)


# In[16]:


# Verify if Alice's and Bob's key bits match
if alice_key == bob_key:
    print("Matching key bits:", bin(alice_key)[2:])
else:
    print("Key bits do not match. Secure communication may be compromised.")


# In[ ]:




