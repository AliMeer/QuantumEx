# QuantumEx
Exploring the Quantum realm, programmatically

## Basic transpiler
`transpile.py` and `transpile.ipynb`

Generate a random quantum circuit and transpile to a circuit comprising of restricted set of gates.

Basic gates for the input circuit: I, H, X, Y, Z, RX, RY, RZ, CNOT, CZ

The output circuit consists of only the following gates: RX, RZ, CZ

The original quantum circuit is replaced by an equivalent combination of gates coming from the restricted set (RX, RZ, CZ) only.



## Circuit Implementation that returns |01> and |10> with a probability of 50% for each.

`produce0110.ipynb`

The approach followed is to create bell states, then employ GD for 1, 10, 100 and 1000 iterations to meet with the output goals.

A random circuit based on gates and introduced noise into circuit and implemented a GD.

## 4-qubit Grover’s algorithm

There are a lot of implementations available for 2 and 3 bit implementations. This is a 4-qubit Grover's algorithm for the ibmqx5.