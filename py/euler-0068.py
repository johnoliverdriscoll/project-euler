from sys import argv

n = int(argv[1])

# The solution requires that the minimum external node be as large as possible.
# We define the sequence of external nodes in decreasing order:

E = list(reversed(range(n + 1, 2 * n + 1)))

# Consequently, the set of inner nodes must contain the lesser half of values
# {1,...,n}. In order to define this sequence, we first define the sequence
# of edges which represent the sums of adjacent internal nodes:

e = list(range(2 + (n - 1) // 2, (3 * n + 1) // 2 + 1))

# We then define the sequence of inner nodes starting with 1 between the pair of
# least edges, subtracting the previous node from the current edge for each
# subsequent index as we circle the ring clockwise:

I = [1]
for i in range(1, n):
  I.append(e[i] - I[i - 1])

# We now need to correct the node sequence orders so that we start building our
# solution set on the maximum edge, producing the external node with the minimal
# value first. This is achieved by simply rotating the sequences:

Ep = E[-1:] + E[:-1]
Is = I[-2:] + I[:-2]
Ip = I[-1:] + I[:-1]

# The final solution is a flattened zip of the ordered sequences:

print(''.join([str(x) for y in zip(Ep, Is, Ip) for x in y]))
