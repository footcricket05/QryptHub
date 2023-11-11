#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram


# In[2]:


# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)


# In[3]:


# Apply Hadamard gates to create superposition
qc.h(0)
qc.h(1)


# In[4]:


# Apply controlled-X (CNOT) gates for entanglement
qc.cx(0, 1)
qc.cx(1, 2)


# In[5]:


# Apply controlled-Z (CZ) gate for further entanglement
qc.cz(0, 2)


# In[6]:


# Measure all qubits
qc.measure_all()


# In[7]:


# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1024)
result = job.result()


# In[8]:


# Get the measurement results
counts = result.get_counts()
print("Measurement results:", counts)


# In[11]:


# Visualize the circuit
qc.draw(output="mpl")


# In[ ]:




