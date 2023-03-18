def combinate(t, d, memo = dict()):
  if len(d) == 0:
    return set()
  if not (t, d) in memo:
    f = set()
    for i in range(0, len(d)):
      c = 1
      while c * d[i] <= t:
        if c * d[i] == t:
          f.add(((d[i], c),))
        else:
          for e in combinate(t - c * d[i], d[i + 1:], memo):
            f.add(tuple(sorted(((d[i], c),) + e, key=lambda t: t[0])))
        c += 1
    memo[(t, d)] = f
  return memo[(t, d)]

print(len(combinate(200, (1, 2, 5, 10, 20, 50, 100, 200))))
