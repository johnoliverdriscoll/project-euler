from sys import argv

def pentagonal(n):
  return (3 * n * n - n) // 2

def p(n, p=[1, 1], pentagonals=list()):
  if n >= len(p):
    i = len(pentagonals)
    while len(pentagonals) == 0 or pentagonals[-1] <= n:
      if i % 2:
        pentagonals.append(pentagonal(-i // 2))
      else:
        pentagonals.append(pentagonal(i // 2 + 1))
      i += 1
    for m in range(len(p), n + 1):
      partitions = 0
      i = 0
      while pentagonals[i] <= m:
        if (i // 2) % 2:
          partitions -= p[m - pentagonals[i]]
        else:
          partitions += p[m - pentagonals[i]]
        i += 1
      p.append(partitions)
  return p[n]

def count_summations(n):
  if n < 2:
    return 1
  return p(n) - 1

n = int(argv[1])
print(count_summations(n))
