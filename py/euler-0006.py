import sys
n = int(sys.argv[1])
sum_of_squares = 0
for x in range(1, n + 1):
  sum_of_squares += x ** 2
s = 0
for x in range(1, n + 1):
  s += x
square_of_sum = s ** 2
print(square_of_sum - sum_of_squares)
