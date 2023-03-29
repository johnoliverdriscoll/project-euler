from os import path

f = open(path.join(path.dirname(__file__), '../resources/p081_matrix.txt'))
m = [[int(c) for c in l.strip().split(',')] for l in f]
x = [i for i in range(0, len(m))] + [len(m) - 1] * (len(m) - 1)
y = [0] * (len(m) - 1) + [i for i in range(0, len(m))]
d = [
  [m[i[0] - j][i[1] + j] for j in range(0, 1 + i[0] - i[1])]
  for i in list(zip(x, y))
]
u = d[-1]
for i in reversed(range(0, len(d) - 1)):
  u = [
    (d[i][j] + u[j] if j == 0
     else d[i][j] + u[j - 1] if j == len(u)
     else d[i][j] + u[j - 1] if d[i][j] + u[j - 1] < d[i][j] + u[j]
     else d[i][j] + u[j])
    if i >= len(d) // 2
    else d[i][j] + u[j] if d[i][j] + u[j] < d[i][j] + u[j + 1]
    else d[i][j] + u[j + 1]
    for j in range(0, len(d[i]))
  ]
print(u[0])
