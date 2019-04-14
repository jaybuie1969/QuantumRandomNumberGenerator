"""
This file is a procedural Python script that demonstrates the use of a quantum-based random integer generator that I wrote
"""
import com.buie.quantum.factories

# Set the size of the random integer being generated, in bits
bits = 40

# Initialize a dictionary to hold any desired weighting of the individual bit generators
# By default, each bit has a 50-50 chance of being a zero or a one, this weighting dictionary can change any desired bits' probabilities
# Keys are integers from 0 to (bits - 1), and the values are integer or floating-point numbers from 0 to 100, indicating the probability of that particular bit returning a one
bitWeights = {
}

# GET YOUR IBM Q EXPERIENCE API TOKEN AT https://quantumexperience.ng.bluemix.net/qx/
apiToken = ""


# Initialize a factory for producing a quantum-derived random ASCII "bit" string and produce 10 random strings
bitStringGenerator = com.buie.quantum.factories.RandomBitStringFactory(bits=bits, weights=bitWeights, apiToken=apiToken)
print("bitStringGenerator = {0}".format(bitStringGenerator))
for i in range(10):
	randomString = bitStringGenerator.get()
	print("{: 02d} - {} - {}".format((i + 1), randomString, len(randomString)))


print("\n\n")


# Initialize a factory for producing a quantum-derived random integer and produce 10 random integers
integerGenerator = com.buie.quantum.factories.RandomIntegerFactory(bits=16, weights=bitWeights, apiToken=apiToken)
print("integerGenerator = {0}".format(integerGenerator))
for i in range(10):
	randomInteger = integerGenerator.get()
	print("{: 2d} - {}".format((i + 1), randomInteger))


print("\n\n")


# Initialize a factory for producing a quantum-derived random floating-point number and produce 10 random floats
floatGenerator = com.buie.quantum.factories.RandomFloatFactory(bits=4, weights=bitWeights, apiToken=apiToken)
print("integerGenerator = {0}".format(floatGenerator))
for i in range(10):
	randomFloat = floatGenerator.get()
	print("{: 2d} - {}".format((i + 1), randomFloat))


print("\n\n")


# Initialize a factory for producing a quantum-derived random integer reciprocal number and produce 10 random reciprocals
reciprocalGenerator = com.buie.quantum.factories.RandomReciprocalFactory(bits=4, weights=bitWeights, apiToken=apiToken)
print("reciprocalGenerator = {0}".format(reciprocalGenerator))
for i in range(10):
	randomReciprocal = reciprocalGenerator.get()
	print("{: 2d} - {}".format((i + 1), randomReciprocal))


print("\n\n")
