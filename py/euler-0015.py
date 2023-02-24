import sys

def lattice_paths_count(n, m, memo = None):
  if memo == None:
    memo = dict()
  if n == 1:
    return m + 1
  if m == 1:
    return n + 1
  if (n, m) in memo:
    return memo[(n, m)]
  memo[(n, m)] = lattice_paths_count(n - 1, m, memo) + lattice_paths_count(n, m - 1, memo)
  return memo[(n, m)]

n = int(sys.argv[1])
print(lattice_paths_count(n, n))
# You could also use `scipy.special.binom(2 * n, n)` for this, but where's the fun in that?
