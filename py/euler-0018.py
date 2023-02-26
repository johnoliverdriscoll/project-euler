import os
t = """
   3
  7 4
 2 4 6
8 5 9 3
"""
t = list(map(lambda l: list(map(int, l.strip().split(' '))), filter(len, t.split('\n'))))
u = t[-1]
for i in reversed(range(0, len(t) - 1)):
  u = list(map(lambda j: t[i][j] + u[j] if t[i][j] + u[j] > t[i][j] + u[j + 1] else t[i][j] + u[j + 1], range(0, i + 1)))
print(u[0])
