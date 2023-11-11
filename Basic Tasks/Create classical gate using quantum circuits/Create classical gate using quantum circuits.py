#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_histogram


# In[2]:


# Create a quantum circuit with 3 qubits (2 for input and 1 for output)
qc = QuantumCircuit(3, 3)  # Specify 3 classical bits for measurement results


# In[3]:


# Apply a Toffoli gate (controlled-controlled-X) to simulate the AND gate
qc.ccx(0, 1, 2)


# In[4]:


# Measure the output qubit and store the result in the classical bit
qc.measure(2, 2)


# In[5]:


# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1024)
result = job.result()


# In[6]:


# Get the measurement results
counts = result.get_counts()
print("Measurement results:", counts)


# In[7]:


# Visualize the circuit
qc.draw(output="mpl")


# In[ ]:




