from sys import argv

n = int(argv[1])

# The solution requires that the minimum external node be as large as possible.
# We define the sequence of external nodes in descending order:

E = [1 + 2 * n - i for i in range(1, n + 1)]

# We then define the sequence of inner nodes starting with 1 between the pair of
# least edges, subtracting the previous node from the current edge for each
# subsequent index as we circle the ring clockwise:

I = [(i + 1) // 2 if i % 2 else (n + i + 1) // 2 for i in range(1, n + 1)]

# In order to produce a solution set that starts with the minimal external node,
# we start building from the maximal edge by shifting `E` and `I` to the right:

E_p = E[-1:] + E[:-1]
I_s = I[-2:] + I[:-2]
I_p = I[-1:] + I[:-1]

# The final solution is a flattened zip of the ordered sequences:

print(''.join([str(x) for y in zip(E_p, I_s, I_p) for x in y]))
