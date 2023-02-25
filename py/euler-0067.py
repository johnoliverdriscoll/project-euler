from os import path
f = open(path.join(path.dirname(__file__), '../fixtures/p067_triangle.txt'))
t = []
while True:
  l = f.readline()
  if not l:
    break
  t.append(list(map(lambda s: int(s), l.strip().split(' '))))
u = t[-1]
for i in reversed(range(0, len(t) - 1)):
  u = list(map(lambda j: t[i][j] + u[j] if t[i][j] + u[j] > t[i][j] + u[j + 1] else t[i][j] + u[j + 1], range(0, i + 1)))
print(u[0])
