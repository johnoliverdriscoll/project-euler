from sys import argv

def next_collatz(n):
  if n % 2 == 0:
    return n // 2
  return 3 * n + 1

def collatz_chain_len(n, memo):
  l = 1
  m = n
  while n != 1:
    if n in memo:
      l += memo[n]
      break
    n = next_collatz(n)
    l += 1
  memo[m] = l
  return l

n = int(argv[1])
i, l, z = 1, 1, 1
memo = dict()
while i < n:
  m = collatz_chain_len(i, memo)
  if m > l:
    l = m
    z = i
  i += 1
print(z)
