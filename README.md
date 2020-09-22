# QuantumEx
Exploring the Quantum realm, programmatically

## Basic transpiler
`transpile.py` and `transpile.ipynb`

Generate a random quantum circuit and transpile to a circuit comprising of restricted set of gates.

Basic gates for the input circuit: I, H, X, Y, Z, RX, RY, RZ, CNOT, CZ

The output circuit consists of only the following gates: RX, RZ, CZ

The original quantum circuit is replaced by an equivalent combination of gates coming from the restricted set (RX, RZ, CZ) only.

