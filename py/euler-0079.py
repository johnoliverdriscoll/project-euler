from os import path

f = open(path.join(path.dirname(__file__), '../resources/p079_keylog.txt'))
keylog = [[int(c) for c in l.strip()] for l in f]
weights = dict()
for key in keylog:
  d = weights.get(key[1], (set(), set()))
  d[0].add(key[0])
  d[1].add(key[2])
  weights[key[1]] = d
digits = list(weights.keys())
start = [x for x in weights if len(weights[x][0]) == 1][0]
end = [x for x in weights if len(weights[x][1]) == 1][0]
key = [list(weights[start][0])[0], start]
curr = start
while curr != end:
  w = [d for d in digits if d != curr]
  left = [len(weights[d][0] ^ set(key)) for d in w]
  curr = w[left.index(min(left))]
  key.append(curr)
key += weights[end][1]
print(''.join([str(d) for d in key]))
