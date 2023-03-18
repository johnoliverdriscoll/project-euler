m = 0
for i in range(1, 100):
  for j in range(1, 100):
    m = max(m, sum([int(c) for c in str(i ** j)]))
print(m)
