import sys

def is_prime(n):
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      return False
  return True

n = int(sys.argv[1])
s = 0
p = 2
while p < n:
  if is_prime(p):
    s += p
  if p > 2:
    p += 2
  p |= 1
print(s)
