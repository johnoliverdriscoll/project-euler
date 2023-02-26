d = dict()
for a in range(1, 1001):
  for b in range(a, 1001):
    if a + 2 * b > 1000:
      break
    for c in range(b, 1001):
      if a + b + c > 1000:
        break
      if a ** 2 + b ** 2 == c ** 2:
        d[a + b + c] = d.get(a + b + c, 0) + 1
print(next(reversed(sorted(d.items(), key=lambda t: t[1])))[0])
