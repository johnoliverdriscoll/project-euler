from sys import argv

n = int(argv[1])
# Closed form derived using Wolfram Alpha.
print(int(4 * n ** 3 + 3 * n ** 2 + 8 * n - 9) // 6)
