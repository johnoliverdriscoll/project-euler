from sys import argv

n = int(argv[1])
f_0 = 1
f_1 = 1
i = 2
while len(str(f_1)) < n:
  f_0, f_1, i = f_1, f_0 + f_1, i + 1
print(i)
