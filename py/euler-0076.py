from sys import argv

def permutate_sum(n, m=None, memo=dict()):
  if n <= 1:
    return 1
  if m == None:
    m = n
  if not (n, m) in memo:
    count = 0
    for i in range(1, m):
      count += permutate_sum(n - i, min(n - i + 1, i + 1))
    memo[(n, m)] = count
  return memo[(n, m)]

n = int(argv[1])
print(permutate_sum(n))
