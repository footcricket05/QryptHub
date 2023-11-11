#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_histogram


# In[2]:


# Create a quantum circuit with 5 qubits
qc = QuantumCircuit(5)


# In[3]:


# Apply Hadamard gates to create superposition on all 5 qubits
for qubit in range(5):
    qc.h(qubit)


# In[4]:


# Apply controlled-X (CNOT) gates to create entanglement
for control_qubit in range(4):
    target_qubit = control_qubit + 1
    qc.cx(control_qubit, target_qubit)


# In[5]:


# Measure all qubits
qc.measure_all()


# In[6]:


# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1024)
result = job.result()


# In[7]:


# Get the measurement results
counts = result.get_counts()
print("Measurement results:", counts)


# In[8]:


# Visualize the circuit
qc.draw(output="mpl")

