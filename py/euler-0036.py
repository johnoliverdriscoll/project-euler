def is_prime(n, p = set()):
  if n in p:
    return True
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      return False
  p.add(n)
  return True

def lstrip(n):
  d = str(n)
  while len(d) > 1:
    d = d[1:]
    yield int(d)

def rstrip(n):
  d = str(n)
  while len(d) > 1:
    d = d[:-1]
    yield int(d)

s = 0
c = 0
n = 2
while True:
  if n > 10 and is_prime(n):
    if sum(map(is_prime, lstrip(n))) == len(str(n)) - 1 and sum(map(is_prime, rstrip(n))) == len(str(n)) - 1:
      s += n
      c += 1
      if c == 11:
        print(s)
        exit()
  n += 1
