m = 0
for i in range(1, 100):
  for j in range(1, 100):
    m = max(m, sum(map(int, str(i ** j))))
print(m)
