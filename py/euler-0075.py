def pythagorean_triple(k, m, n):
  return k * 2 * m * n, k * (m ** 2 - n ** 2), k * (m ** 2 + n ** 2)

triples = set()
n = 1
while 1:
  m = n + 1
  while 1:
    k = 1
    while 1:
      t = pythagorean_triple(k, m, n)
      if (L := sum(t)) <= 1500000:
        triples.add(tuple(sorted(t)))
        k += 1
      else:
        break
    if k == 1:
      break
    m += 1
  if m == n + 1:
    break
  n += 1
counts = dict()
for triple in triples:
  L = sum(triple)
  counts[L] = counts.get(L, 0) + 1
count = 0
for L in counts:
  if counts[L] == 1:
    count += 1
print(count)
