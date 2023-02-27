def permutate(s, not_first = '0'):
  if len(s) == 1:
    yield s
  else:
    for i in range(0, len(s)):
      if not_first == None or s[i] != not_first:
        for p in permutate(s[:i] + s[i + 1:], None):
          yield s[i] + p

def is_prime(n, p = dict()):
  if n in p:
    return p[n]
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      p[n] = False
      break
  if not n in p:
    p[n] = True
  return p[n]

def prime_permutations(n, v = set()):
  if n in v:
    return
  p = list(set(map(int, permutate(str(n)))))
  v |= set(p)
  i = 0
  while i < len(p) - 3:
    j = i + 1
    while j < len(p) - 2:
      d = abs(p[i] - p[j])
      t = [p[i] + m * d for m in range(0, 3)]
      if set(t) & set(p) == set(t) and sum(map(is_prime, t)) == 3:
        return sorted(t)
      j += 1
    i += 1

for n in range(1000, 10000):
  p = prime_permutations(n)
  if p:
    print(''.join(map(str, p)))
