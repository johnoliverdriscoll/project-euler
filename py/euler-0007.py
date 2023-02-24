import sys
n = int(sys.argv[1])
c = 0
p = 2
while True:
  is_prime = True
  for x in range(2, int(p ** (1 / 2)) + 1):
    if p % x == 0:
      is_prime = False
      break
  if is_prime:
    c += 1
    if c == n:
      print(p)
      exit()
  if p > 2:
    p += 2
  p |= 1
