def permutations(count):
  if count == 1 or count == 2:
    return count
  p = 2
  for i in range(3, count + 1):
    p *= i
  return p

def permutation(digits, i):
  if i == 1 or len(digits) == 1:
    return digits
  for j in range(0, len(digits)):
    n = permutations(len(digits) - 1)
    if i > n:
      i -= n
    else:
      return [digits[j]] + permutation(digits[0:j] + digits[j + 1:], i)

p = [str(n) for n in permutation([int(c) for c in '0123456789'], 1000000)]
print(''.join(p))
