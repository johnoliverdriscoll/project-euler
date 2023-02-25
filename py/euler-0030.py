import sys
e = int(sys.argv[1])
d = [0] * (e + 1)
t = 0
while d != [9] * (e + 1):
  i = 0
  while i < e and d[i] == d[i + 1]:
    i += 1
  if len(set(d[:i])) == 1:
    d = [0] * i + [d[i] + 1] + d[i + 1:]
  else:
    d[i] += 1
  if len(set(d) - set([0])) > 1:
    r = sum(map(lambda n: n ** e, d))
    s = '0' * (e + 1 - len(str(r))) + str(r)
    u = d.copy()
    for c in s:
      if int(c) in u:
        u.remove(int(c))
    if len(u) == 0:
      t += r
print(t)
