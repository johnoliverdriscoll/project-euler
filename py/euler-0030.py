from sys import argv

e = int(argv[1])
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
    r = sum([n ** e for n in d])
    s = '0' * (e + 1 - len(str(r))) + str(r)
    u = d.copy()
    for c in s:
      u.discard(int(c))
    if len(u) == 0:
      t += r
print(t)
