import sys
n = int(sys.argv[1])
s = 0
p = 2
while p < n:
  is_prime = True
  for x in range(2, int(p ** (1 / 2)) + 1):
    if p % x == 0:
      is_prime = False
  if is_prime:
    s += p
  if p > 2:
    p += 2
  p |= 1
print(s)
