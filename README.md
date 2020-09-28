# QuantumEx
Exploring the Quantum realm, programmatically

## Basic transpiler
`transpile.py` and `transpile.ipynb`

Generate a random quantum circuit and transpile to a circuit comprising of restricted set of gates.

Basic gates for the input circuit: I, H, X, Y, Z, RX, RY, RZ, CNOT, CZ

The output circuit consists of only the following gates: RX, RZ, CZ

The original quantum circuit is replaced by an equivalent combination of gates coming from the restricted set (RX, RZ, CZ) only.



## Circuit Implementation that returns |01> and |10> with a probability of 50% for each.

The approach followed is to create bell states, then employ GD for 1, 10, 100 and 1000 iterations to meet with the output goals.

Currently facing issues in creation of bell state for a generic circuit equation. As for GD a polynomial cost function is required.

I am unable to come with the right command combination at the moment.
