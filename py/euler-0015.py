from sys import argv

def lattice_paths_count(n, m, memo = None):
  if n == 1:
    return m + 1
  if m == 1:
    return n + 1
  if memo == None:
    memo = dict()
  l = memo.get((n, m), None)
  if l == None:
    l = lattice_paths_count(n - 1, m, memo) \
      + lattice_paths_count(n, m - 1, memo)
    memo[(n, m)] = l
  return l

n = int(argv[1])
# You could also use `scipy.special.binom(2 * n, n)` for this, but where's
# the fun in that?
print(lattice_paths_count(n, n))
