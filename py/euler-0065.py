from sys import argv

def denominator(i):
  if i == 1:
    return 2
  if i % 3 == 0:
    return 2 * i // 3
  return 1

r = int(argv[1])
n = 1
d = denominator(r)
for i in reversed(range(1, r)):
  n += d * denominator(i)
  n, d = d, n
print(sum([int(c) for c in str(d)]))
