def to_bits(n):
  bits = []
  while n:
    bits.append(n % 2)
    n //= 2
  return bits[::-1]

def is_palindrome(l):
  c = l.copy()
  while len(c) > 1:
    if not c.pop(0) == c.pop():
      return False
  return True

print(sum(filter(lambda n: is_palindrome(list(str(n))) and is_palindrome(to_bits(n)), range(1, 1000000))))
