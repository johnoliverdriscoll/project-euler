from os import path

f = open(path.join(path.dirname(__file__), '../resources/p081_matrix.txt'))
m = [[int(c) for c in l.strip().split(',')] for l in f]
u = [r[-1] for r in m]
for c in reversed(range(0, len(m) - 1)):
  v = []
  for r in range(0, len(m)):
    choices = []
    if r > 0:
      s = m[r][c]
      above = []
      for ar in reversed(range(0, r)):
        s += m[ar][c]
        above.append(s + u[ar])
      choices.append(min(above))
    choices.append(m[r][c] + u[r])
    if r < len(m) - 1:
      s = m[r][c]
      below = []
      for br in range(r + 1, len(m)):
        s += m[br][c]
        below.append(s + u[br])
      choices.append(min(below))
    v.append(min(choices))
  u = v
print(min(u))
