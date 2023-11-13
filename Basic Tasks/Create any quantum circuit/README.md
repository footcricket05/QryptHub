# Quantum Circuit 

This repository contains a quantum circuit implemented using Qiskit, a quantum computing library in Python. The circuit is designed to showcase the creation of a superposition and entanglement on a 5-qubit quantum system.

## Usage

1. Install the required dependencies:

    ```bash
    pip install qiskit
    ```

2. Run the quantum circuit simulation:

    ```bash
    python "Create any quantum circuit.py"
    ```

    This will execute the provided Qiskit code, simulate the quantum circuit, and display measurement results.

## Circuit Description

- The circuit consists of 5 qubits.
- Hadamard gates are applied to each qubit to create a superposition state.
- Controlled-X (CNOT) gates are applied to create entanglement between adjacent qubits.
- All qubits are measured at the end of the circuit.

## Results

The simulation results will be displayed, showing the counts of each measurement outcome. The measurement results represent the probabilities of finding the quantum system in different states.

## About Qiskit

[Qiskit](https://qiskit.org/) is an open-source quantum computing software development framework developed by IBM.

## License

This project is licensed under the [MIT License](LICENSE).
