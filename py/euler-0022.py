from functools import cmp_to_key
from locale import strcoll
from os import path

f = open(path.join(path.dirname(__file__), '../resources/p022_names.txt'))
names = sorted(
  [name.strip('"') for name in f.readline().split(',')],
  key=cmp_to_key(strcoll),
)
s = 0
for i in range(0, len(names)):
  s += (1 + i) * sum([1 + ord(c) - ord('A') for c in names[i]])
print(s)
