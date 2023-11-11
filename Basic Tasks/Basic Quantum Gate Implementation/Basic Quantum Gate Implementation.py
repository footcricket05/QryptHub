#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import necessary libraries
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram


# In[5]:


# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)


# In[6]:


# Apply basic quantum gates
qc.h(0)  # Hadamard gate on qubit 0
qc.cx(0, 1)  # CNOT gate (controlled-X) with qubit 0 as the control and qubit 1 as the target


# In[7]:


# Measure the qubits
qc.measure_all()


# In[10]:


# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1024)
result = job.result()


# In[11]:


# Get the measurement results
counts = result.get_counts()
print("Measurement results:", counts)


# In[20]:


# Visualize the circuit
qc.draw(output="text")

