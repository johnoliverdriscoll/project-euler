# This a great example of over-engineering.
# The simpler, faster solution (although requiring more memory) is to
# build a list of perfect cubes with their digits sorted canonically.
# When the fifth occurence of a canonically sorted perfect cube is
# added, the cubed index of its first occurrence is the answer.
#
# As for this solution: Build a tree of perfect cubes where each node
# may have a child for each digit in the cube. A node may be marked
# as a leaf, indicating that it is a terminating digit. After each
# cube is added to the tree, build the intersection between it and
# the permutations of the cube. The first cube whose intersection has
# five leaves is the answer.
from sys import argv
from math import log10

class Node:

  def __init__(self):
    self.leaf = False
    self.children = [None] * 10

  def add(self, digits):
    if len(digits) == 0:
      self.leaf = True
    else:
      if not self.children[digits[0]]:
        self.children[digits[0]] = Node()
      self.children[digits[0]].add(digits[1:])

  def permutate(self, s, not_first=0):
    node = Node()
    if len(s) == 0 and self.leaf:
      node.leaf = True
    else:
      for i in range(0, len(s)):
        if not_first == None or s[i] != not_first:
          if not node.children[s[i]] and self.children[s[i]]:
            node.children[s[i]] = self.children[s[i]].permutate(
              s[:i] + s[i + 1:],
              None,
            )
    return node

  def leaves(self):
    leaves = 1 if self.leaf else 0
    for i in range(0, 10):
      if self.children[i]:
        leaves += self.children[i].leaves()
    return leaves

  def least_path(self):
    if self.leaf:
      return []
    for i in range(0, 10):
      if self.children[i]:
        path = self.children[i].least_path()
        if path != None:
          return [i] + path

def tuple_to_int(d):
  return sum([t[0] * 10 ** t[1] for t in zip(d, reversed(range(0, len(d))))])

def int_to_tuple(n):
  l = tuple()
  for i in range(0, int(log10(n) + 1)):
    l = (n % 10,) + l
    n //= 10
  return l

n = int(argv[1])
x = 1
node = Node()
while 1:
  x3 = x ** 3
  t = int_to_tuple(x3)
  node.add(t)
  common = node.permutate(t)
  if common.leaves() == n:
    print(tuple_to_int(common.least_path()))
    exit()
  x += 1
