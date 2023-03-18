def d(n):
  i = 1
  f = ''
  for j in n:
    while len(f) < j:
      f += str(i)
      i += 1
    yield int(f[j - 1])

p = 1
for d_n in d([1, 100, 1000, 10000, 100000, 1000000]):
  p *= d_n
print(p)
