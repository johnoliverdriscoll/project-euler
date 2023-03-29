from os import path

f = open(path.join(path.dirname(__file__), '../resources/p067_triangle.txt'))
t = [[int(c) for c in l.strip().split(' ')] for l in f]
u = t[-1]
for i in reversed(range(0, len(t) - 1)):
  u = [
    t[i][j] + u[j] if t[i][j] + u[j] > t[i][j] + u[j + 1]
    else t[i][j] + u[j + 1]
    for j in range(0, i + 1)
  ]
print(u[0])
