from itertools import permutations

f = set()
for p in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]):
  for i in range(1, 8):
    for j in range(i + 1, 8):
      a = int(''.join([str(n) for n in p[:i]]))
      b = int(''.join([str(n) for n in p[i:j]]))
      c = int(''.join([str(n) for n in p[j:]]))
      if a * b == c:
        f.add(c)
print(sum(f))
