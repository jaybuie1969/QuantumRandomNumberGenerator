# QuantumRandomNumberGenerator
This is a fairly simple library of four random number generators that produce a random number based on the collapse of quantum superposition states into zeros and ones.  A bit is generated for each quantum state that gets collapsed.

This library includes four different random number factories:
*	A random N-character text string of ones and zeros, suitable for saving out as an ASCII text file
*	A random N-bit integer
*	A random floating-point number produced by dividing a random N-bit integer by 2^N
*	A random floating-point number produced by taking the reciprocal of a random (N-bit integer + 1)

Each of the N qubits is placed in a quantum superposition state.  By default, the qubit is placed in a 50/50 superposition.  However, each bit can be individually “tuned” to improve its chances of producing either a zero or a one.

Each bit is placed in a superposition by applying a Hadamard – U1(rotation) – Hadamard gate series to each qubit.  Using a default rotation of π/2 provides the 50/50 probability.  Decreasing the U1() rotation increases the chance of the qubit collapsing to a zero, and increasing it increases the chance of collapsing to one.
