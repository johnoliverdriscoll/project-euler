def pentagonal(n):
  return (3 * n * n - n) // 2

def p(n, p=[1, 1], pentagonals=list()):
  if n >= len(p):
    i = len(pentagonals)
    while len(pentagonals) == 0 or pentagonals[len(pentagonals) - 1] <= n:
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

k = 0
while 1:
  n = 5 * k + 4
  p_n = p(n)
  if p_n % 1000000 == 0:
    print(n)
    exit()
  k += 1
