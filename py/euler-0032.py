def permutate(d):
  if len(d) == 1:
    yield d
  else:
    for i in range(0, len(d)):
      for p in permutate(d[:i] + d[i + 1:]):
        yield [d[i]] + p

f = set()
for p in permutate([1, 2, 3, 4, 5, 6, 7, 8, 9]):
  for i in range(1, 8):
    for j in range(i + 1, 8):
      a = int(''.join(map(str, p[:i])))
      b = int(''.join(map(str, p[i:j])))
      c = int(''.join(map(str, p[j:])))
      if a * b == c:
        f.add(c)
print(sum(f))
