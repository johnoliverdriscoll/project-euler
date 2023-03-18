from sys import argv

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

def prime():
  yield 2
  n = 3
  while 1:
    if is_prime(n):
      yield n
    n += 2

n = int(argv[1])
p = []
it = prime()
m = 0
c = 0
while 1:
  p.append(next(it))
  if sum(p[-c:]) > n:
    break
  i, j, l = 0, 0, 0
  while i < len(p):
    s = sum(p[i:])
    i += 1
    if s < n and is_prime(s):
      j = len(p) - i
      l = s
      break
  if c < j:
    m = l
    c = j
print(m)
