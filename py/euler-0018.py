import os

t = """
   3
  7 4
 2 4 6
8 5 9 3
"""
t = [[int(n) for n in l.strip().split(' ')] for l in t.split('\n') if len(l)]
u = t[-1]
for i in reversed(range(0, len(t) - 1)):
  u = [t[i][j] + u[j] if t[i][j] + u[j] > t[i][j] + u[j + 1]
       else t[i][j] + u[j + 1] for j in range(0, i + 1)]
print(u[0])
