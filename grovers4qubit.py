from qiskit import QuantumCircuit, Aer, execute
import math
pi = math.pi

qcirc = QuantumCircuit(4, 4)


# 
# State Preparation
# 
qcirc.h(0)
qcirc.h(1) 
qcirc.h(2) 
qcirc.h(3)

# 
# Oracle for 0010
# 
qcirc.x(0) 
qcirc.x(2) 
qcirc.x(3)
qcirc.cu1(pi/4, 0, 3) 
qcirc.cx(0, 1) 
qcirc.cu1(-pi/4, 1, 3)
qcirc.cx(0, 1) 
qcirc.cu1(pi/4, 1, 3) 
qcirc.cx(1, 2) 
qcirc.cu1(-pi/4, 2, 3) 
qcirc.cx(0, 2) 
qcirc.cu1(pi/4, 2, 3) 
qcirc.cx(1, 2) 
qcirc.cu1(-pi/4, 2, 3) 
qcirc.cx(0, 2) 
qcirc.cu1(pi/4, 2, 3)
qcirc.x(0) 
qcirc.x(2) 
qcirc.x(3)

# 
# Amplify
# 

qcirc.h(0) 
qcirc.h(1) 
qcirc.h(2) 
qcirc.h(3)
qcirc.x(0) 
qcirc.x(1) 
qcirc.x(2) 
qcirc.x(3)

#
# Troffoli Gate
# 

qcirc.cu1(pi/4, 0, 3) 
qcirc.cx(0, 1) 
qcirc.cu1(-pi/4, 1, 3) 
qcirc.cx(0, 1) 
qcirc.cu1(pi/4, 1, 3) 
qcirc.cx(1, 2) 
qcirc.cu1(-pi/4, 2, 3) 
qcirc.cx(0, 2) 
qcirc.cu1(pi/4, 2, 3) 
qcirc.cx(1, 2)

qcirc.cu1(-pi/4, 2, 3) 
qcirc.cx(0, 2) 
qcirc.cu1(pi/4, 2, 3) 


# 
# Amplify
# 


qcirc.x(0) 
qcirc.x(1) 
qcirc.x(2) 
qcirc.x(3)
qcirc.h(0) 
qcirc.h(1) 
qcirc.h(2) 
qcirc.h(3)

# 
# Measure Results
#

qcirc.measure([0,1,2,3], [0,1,2,3]) 

qasm_sim = Aer.get_backend('qasm_simulator')
job = execute(qcirc, qasm_sim, shots=1000)
result = job.result()
count = result.get_counts()

print(count)
