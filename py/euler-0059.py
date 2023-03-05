from os import path

# Produce frequency table for each element of a list `m`.
def freq_table(m):
  f = dict()
  for c in m:
    f[c] = f.get(c, 0) + 1
  return f

# Iterate over permutations of a list `s`.
def permutate(s):
  if len(s) == 1:
    yield s
  else:
    for i in range(0, len(s)):
      for p in permutate(s[:i] + s[i + 1:]):
        yield [s[i]] + p

# Returns the number of letters in a string `s`.
def count_letters(s):
  return sum(map(lambda c: (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'), s))

# Parse input as list of ints.
file = open(path.join(path.dirname(__file__), '../resources/p059_cipher.txt'))
ct = list(map(int, file.readline().split(',')))
# Build character frequency table.
f = freq_table(ct)
# Produce sorted list of (value, occurence count) tuples for every character
# in the ciphertext.
w = list(map(lambda v: v[0], list(sorted(f.items(), key=lambda v: v[1]))))
# The three most frequently occurring values are likely to be encrypted spaces,
# therefore the key is some permutation of these values XOR the ASCII value for
# a space. The candidates with the most letters is the plaintext.
pt = next(reversed(sorted([
  list(map(lambda v: chr(v[0] ^ key[v[1] % 3]), zip(ct, range(0, len(ct)))))
  for key in permutate(list(map(lambda c: c ^ ord(' '), w[-3:])))
], key=count_letters)))
print(sum(map(ord, pt)))
