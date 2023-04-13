def square_digit_chain_terminator(n, memo=dict()):
  if n == 1 or n == 89:
    return n
  r = memo.get(n, None)
  if r == None:
    r = square_digit_chain_terminator(sum([int(d) ** 2 for d in str(n)]))
    memo[n] = r
  return r

count = 0
for n in range(1, 10000000):
  if square_digit_chain_terminator(n) == 89:
    count += 1
print(count)
