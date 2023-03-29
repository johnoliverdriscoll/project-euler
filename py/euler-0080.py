def sqrt_decimal_expansion_to_n(x, n):
  pairs = []
  while x:
    pairs.append(x % 100)
    x //= 100
  pair = pairs.pop()
  x = int(pair ** (1 / 2))
  rem = pair - x * x
  if rem == 0:
    return []
  decimals = [x]
  while len(decimals) < n:
    x = 10 * (x + (x % 10))
    rem *= 100
    if len(pairs):
      rem += pairs.pop()
    for i in reversed(range(0, 10)):
      if (x + i) * i <= rem:
        decimals.append(i)
        if len(decimals) == n:
          return decimals
        x += i
        rem -= x * i
        break

print(sum([sum(sqrt_decimal_expansion_to_n(i, 100)) for i in range(1, 100)]))
