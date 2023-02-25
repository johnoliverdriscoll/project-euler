import sys

def digits(n):
  d = 0
  while n:
    n //= 10
    d += 1
  return d

def recurring_digits(d):
  n = 1
  m = []
  r = []
  while True:
    b = 0
    while n < d:
      n *= 10
      b += 1
    if n % d == 0:
      return 0
    m.append('0' * (b - 1) + str(n // d))
    if n % d in r:
      return len(''.join(m[r.index(n % d) - len(r):]))
    n = n % d
    r.append(n)

n = int(sys.argv[1])
c = 0
d = None
for i in range(1, n):
  r = recurring_digits(i)
  if r > c:
    c = r
    d = i
print(d)
