l = 1000000000
p = 0

m = 2
while 1:
  n = ((m ** 2 - 1) // 3) ** (1/2)
  if n == int(n):
    n = int(n)
    a, b, c = 2 * m * n, m ** 2 - n ** 2, m ** 2 + n ** 2
    if 2 * b + 2 * c > l:
      break
    p += 2 * b + 2 * c
  m += 1

m = 2
while 1:
  n = 2 * m - (3 * m ** 2 + 1) ** (1/2)
  if n == int(n):
    n = int(n)
    a, b, c = 2 * m * n, m ** 2 - n ** 2, m ** 2 + n ** 2
    if 2 * a + 2 * c > l:
      break
    p += 2 * a + 2 * c
  m += 1

print(p)
