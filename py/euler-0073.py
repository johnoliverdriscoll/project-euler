from sys import argv

# Return the fractional form of a continued fraction as a
# (numerator, denominator) tuple.
def to_frac(f):
  num = 1
  den = f.pop()
  for n in reversed(f):
    num, den = den, den * n + num
  return num, den

# Find the closest approximation to the mediant between a and b with a
# denominator <= d.
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
count = 0
stack = [((1, 3), (1, 2))]
while len(stack):
  a, b = stack.pop()
  if (m := mediant(a, b, d)):
    count += 1
    stack.append((a, m))
    stack.append((m, b))
print(count)
