import sys

def is_prime(n):
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      return False
  return True

n = int(sys.argv[1])
c = 0
p = 2
while True:
  if is_prime(p):
    c += 1
    if c == n:
      print(p)
      exit()
  if p > 2:
    p += 2
  p |= 1
