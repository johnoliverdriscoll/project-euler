from itertools import combinations, permutations
from operator import add, sub, mul, truediv as div

def express(d):
  if len(d) == 1:
    yield d[0]
  else:
    for p in permutations(d):
      for i in range(1, len(d)):
        a, b = p[:i], p[i:]
        for x in express(a):
          for y in express(b):
            for op in (add, sub, mul, div):
              if op == div and y == 0:
                continue
              yield op(x, y)

def max_consecutive_expressible_1_to_n(d):
  r = [False] * 6 * 7 * 8 * 9
  for v in express(d):
    if v > 0 and int(v) == v:
      r[int(v) - 1] = True
  i = 0
  while i < len(r) and r[i]:
    i += 1
  return i

cm, cd = 0, None
for d in combinations(range(0, 10), 4):
  c = max_consecutive_expressible_1_to_n(d)
  if cm < c:
    cm = c
    cd = ''.join([str(n) for n in d])
print(cd)
