from os import path

f = open(path.join(path.dirname(__file__), '../resources/p083_matrix.txt'))
m = [[int(c) for c in l.strip().split(',')] for l in f]
x = [i for i in range(0, len(m))] + [len(m) - 1] * (len(m) - 1)
y = [0] * (len(m) - 1) + [i for i in range(0, len(m))]
d = [
  [m[i[0] - j][i[1] + j] for j in range(0, 1 + i[0] - i[1])]
  for i in list(zip(x, y))
]
u = d[-1]
for i in reversed(range(0, len(d) - 1)):
  v = []
  for j in range(0, len(d[i])):
    choices = []
    if i < len(d) // 2:
      s = sum(d[i][:j]) + sum(d[i + 1][:j + 1])
      for k in range(0, j + 1):
        if k > 0:
          s -= u[k - 1] + d[i][k - 1]
        s += u[k] - d[i + 1][k]
        choices.append(s)
      s = sum(d[i][j + 1:]) + sum(d[i + 1][j + 1:])
      for k in reversed(range(j + 1, len(d[i + 1]))):
        if k < len(d[i + 1]) - 1:
          s -= u[k + 1] + d[i][k]
        s += u[k] - d[i + 1][k]
        choices.append(s)
    else:
      if j > 0:
        s = sum(d[i][1:j]) + sum(d[i + 1][0:j])
        for k in range(0, j):
          if k > 0:
            s -= u[k - 1] + d[i][k]
          s += u[k] - d[i + 1][k]
          choices.append(s)
      if j < len(d[i]) - 1:
        s = sum(d[i][j + 1:-1]) + sum(d[i + 1][j:])
        for k in reversed(range(j, len(d[i + 1]))):
          if k < len(d[i + 1]) - 1:
            s -= u[k + 1] + d[i][k + 1]
          s += u[k] - d[i + 1][k]
          choices.append(s)
    v.append(min(choices) + d[i][j])
  u = v
print(u[0])
