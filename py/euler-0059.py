from itertools import permutations
from os import path

# Produce frequency table for each element of a list `m`.
def freq_table(m):
  f = dict()
  for c in m:
    f[c] = f.get(c, 0) + 1
  return f

# Iterate over permutations of a list `s`.

# Returns the number of letters in a string `s`.
def count_letters(s):
  return sum([(c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z') for c in s])

# Parse input as list of ints.
file = open(path.join(path.dirname(__file__), '../resources/p059_cipher.txt'))
ct = [int(c) for c in file.readline().split(',')]
# Build character frequency table.
f = freq_table(ct)
# Produce sorted list of (value, occurence count) tuples for every character
# in the ciphertext.
w = [v[0] for v in sorted(f.items(), key=lambda v: v[1])]
# The three most frequently occurring values are likely to be encrypted spaces,
# therefore the key is some permutation of these values XOR the ASCII value for
# a space. The candidates with the most letters is the plaintext.
print(sum([ord(c) for c in next(reversed(sorted([
  [chr(v[0] ^ key[v[1] % 3]) for v in zip(ct, range(0, len(ct)))]
  for key in permutations([c ^ ord(' ') for c in w[-3:]])
], key=count_letters)))]))
