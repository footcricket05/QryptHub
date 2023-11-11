#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram


# In[2]:


# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)


# In[3]:


# Apply Hadamard gate to the first qubit
qc.h(0)


# In[4]:


# Apply a CNOT gate with the first qubit as the control and the second qubit as the target
qc.cx(0, 1)


# In[5]:


# Measure both qubits
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
qc.draw(output="text")


# In[ ]:




