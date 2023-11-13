# Quantum Circuit with Multi-State Entanglement

This repository contains a Python implementation of a quantum circuit using Qiskit, a quantum computing library in Python. The circuit showcases the creation of multi-state entanglement through the application of Hadamard gates for superposition, controlled-X (CNOT) gates for entanglement, controlled-Z (CZ) gate for further entanglement, and concludes with measurements.

## Overview

The quantum circuit includes the following key components:

1. **Superposition with Hadamard Gates:**
   - Hadamard gates are applied to qubits 0 and 1 to create a superposition.

2. **Entanglement with Controlled-X (CNOT) Gates:**
   - Controlled-X (CNOT) gates are applied between qubits 0 and 1, as well as qubits 1 and 2, creating entanglement.

3. **Further Entanglement with Controlled-Z (CZ) Gate:**
   - A controlled-Z (CZ) gate is applied between qubits 0 and 2, introducing further entanglement.

4. **Multi-State Entanglement:**
   - The combination of Hadamard gates, controlled-X (CNOT) gates, and controlled-Z (CZ) gate results in multi-state entanglement.

5. **Measurement:**
   - All qubits are measured at the end of the circuit.

6. **Simulation and Results:**
   - The circuit is simulated using Qiskit's Aer backend, and the measurement results are displayed.

## Usage

1. Install the required dependencies:

    ```bash
    pip install qiskit
    ```

2. Run the Quantum Circuit simulation:

    ```bash
    python "Multi state entanglement creation.py"
    ```

    This will execute the provided Qiskit code, simulate the quantum circuit, and display measurement results.

## Results

The simulation results will be displayed, showing the counts of each measurement outcome. In this example, the expected results include states like '110', '000', '001', and '111'.

## About Qiskit

[Qiskit](https://qiskit.org/) is an open-source quantum computing software development framework developed by IBM.

## License

This project is licensed under the [MIT License](LICENSE).
