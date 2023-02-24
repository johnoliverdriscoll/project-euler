import sys
n = int(sys.argv[1])
for x in range(2, n):
  if n % x == 0:
    d = n // x
    is_prime = True
    for y in range(2, 1 + int(d ** (1 / 2))):
      if d % y == 0:
        is_prime = False
        break
    if is_prime:
      print(d)
      exit()
