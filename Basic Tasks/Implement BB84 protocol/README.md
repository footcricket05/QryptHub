# BB84 Quantum Key Distribution (QKD) Simulation

This repository contains a Python implementation of Quantum Key Distribution (QKD) simulation using the BB84 protocol with Qiskit, a quantum computing library in Python. QKD is a cryptographic technique that uses quantum mechanics to secure a communication channel and exchange secret keys between two parties, typically named Alice and Bob.

## Overview

The QKD simulation follows the BB84 protocol and includes the following steps:

1. **Random Bit Generation:**
   - Alice generates a random bitstring and corresponding random bases.
   - Bob chooses random bases for measurements.

2. **Quantum Circuit Setup:**
   - A quantum circuit is created with qubits for Alice's bits and classical bits for measurement results.

3. **Bit Encoding:**
   - Alice encodes her random bitstring onto qubits based on her chosen random bases.

4. **Quantum Communication:**
   - Bob measures the qubits based on his randomly chosen bases.

5. **Filtering Bits:**
   - Alice and Bob compare their chosen bases to filter bits and create a sifted key.

6. **Error Checking:**
   - Error checking is performed to identify any discrepancies in the sifted key.

7. **Privacy Amplification:**
   - Privacy amplification is applied to further enhance the security of the key.

8. **Results:**
   - The simulation displays various results, including Alice's random bitstring, Bob's measurements, the sifted key, measurement results, errors, and the final key after privacy amplification.

## Usage

1. Install the required dependencies:

    ```bash
    pip install qiskit
    ```

2. Run the BB84 QKD simulation:

    ```bash
    python "Implementation of BB84 protocol using a Quantum Key Distribution (QKD) setup"
    ```

    This will execute the provided Qiskit code, simulate the BB84 QKD process, and display the results.

## About Qiskit

[Qiskit](https://qiskit.org/) is an open-source quantum computing software development framework developed by IBM.

## License

This project is licensed under the [MIT License](LICENSE).
