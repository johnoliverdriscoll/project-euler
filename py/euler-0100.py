from sys import argv

n = int(argv[1])
a_2, a_1 = 1, 3
b_2, b_1 = 0, 1
while a_1 + b_1 < n:
  a_2, a_1 = a_1, 6 * a_1 - a_2 - 2
  b_2, b_1 = b_1, 6 * b_1 - b_2
print(a_1)
