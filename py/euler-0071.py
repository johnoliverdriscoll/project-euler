from sys import argv

def to_frac(f):
  num = 1
  den = f.pop()
  for n in reversed(f):
    num, den = den, den * n + num
  return num, den

def mediant(a, b, d):
  num = a[0] + b[0]
  den = a[1] + b[1]
  f = []
  while num > 1:
    n = den // num
    f.append(n)
    num, den = den % num, num
  f.append(den)
  for i in reversed(range(0, len(f) + 1)):
    num, den = to_frac(f[0:i])
    if den <= d:
      break
  if (num, den) == a or (num, den) == b:
    return None
  return num, den

d = int(argv[1])
left, right = (1, d), (3, 7)
while (curr := mediant(left, right, d)) != None:
  left = curr
print(left[0])
