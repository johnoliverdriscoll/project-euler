import sys

def is_figurate(n, d):
  if n == 3:
    return ((1 + 8 * d) ** (1 / 2) - 1) % 2 == 0
  if n == 4:
    return (d ** (1 / 2)) % 1 == 0
  if n == 5:
    return (1 + (1 + 24 * d) ** (1 / 2)) % 6 == 0
  if n == 6:
    return (1 + (1 + 8 * d) ** (1 / 2)) % 4 == 0
  if n == 7:
    return (3 + (9 + 40 * d) ** (1 / 2)) % 10 == 0
  if n == 8:
    return (2 + (4 + 12 * d) ** (1 / 2)) % 6 == 0

def cyclic_figurates(figurates, d, first=None):
  groups = []
  if first == None:
    first = d
  elif d % 100 == first // 100:
    groups.append([d])
  for i in range(0, len(figurates)):
    for x in figurates[i]:
      if d % 100 == x // 100:
        for group in cyclic_figurates(figurates[:i] + figurates[i + 1:], x, first):
          groups.append([d] + group)
  return groups

count = int(sys.argv[1])
figurates = {
  3: set(),
  4: set(),
  5: set(),
  6: set(),
  7: set(),
  8: set(),
}
for d in range(1000, 10000):
  for n in range(3, 9):
    if is_figurate(n, d):
      figurates[n].add(d)
for d in figurates[3]:
  groups = cyclic_figurates(list(figurates.values())[1:], d)
  for group in groups:
    if len(group) == count:
      print(sum(group))
