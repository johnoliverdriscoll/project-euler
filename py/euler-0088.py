from sys import argv

"""
Tree approach:

At the root of the tree for every k is a node with value n where n is a list of
natural numbers.

Every node has the intrinsic properties p=product(n) and s=sum(n).

Every node may have a left and right child node.

A node has a left child if len(n) == 1 or n[-1] < n[-2]. The left child's value
is n[:-1] + [n[-1] + 1].

A node has a right child if len(n) < k. The right child's value is n + [2].

The solution for k is the value of the node where p == s when visiting the nodes
in a breadth-first search of its tree.

Optimizations:

There is no need to store the entire list n. The last two numbers in the list
are all that is needed to generate the tree without duplicate nodes.

The s property is the same for every node of the same depth and increases by 1
for each level of depth.

If a child's p property is greater than it's s property, it does not need to be
queued for visitation, and thus its lineage can be erased from the tree.

Instead of building a unique tree for every value of k, continuously build a
tree while detecting nodes that are minimal solutions for any given k where
2 ≤ k ≤ 12000.
"""

class Node:
  def __init__(self, c, p, s, a, b=None):
    self.c = c
    self.a = a
    self.b = b
    self.p = p
    self.s = s

def minimal_product_sums(K):
  minimal_product_sums = dict()
  nodes = [Node(1, 2, 2, 2)]
  ks = set(range(2, K + 1))
  while len(ks):
    children = []
    for node in nodes:
      if node.c == 1:
        left = Node(
          node.c,
          node.p + node.p // node.a,
          node.s + 1,
          node.a + 1,
        )
        children.append(left)
        right = Node(
          node.c + 1,
          node.p * 2,
          node.s + 2,
          node.a,
          2,
        )
        if right.p <= right.s + K - right.c:
          if right.p >= right.s:
            k = right.p - right.s + right.c
            m = minimal_product_sums.get(k, right.p)
            if m >= right.p:
              minimal_product_sums[k] = right.p
            if k in ks:
              ks.remove(k)
          children.append(right)
      else:
        if node.a > node.b:
          left = Node(
            node.c,
            node.p + node.p // node.b,
            node.s + 1,
            node.a,
            node.b + 1,
          )
          if left.p <= left.s + K - left.c:
            if left.p >= left.s:
              k = left.p - left.s + left.c
              m = minimal_product_sums.get(k, left.p)
              if m >= left.p:
                minimal_product_sums[k] = left.p
              if k in ks:
                ks.remove(k)
            children.append(left)
        if node.c < K:
          right = Node(
            node.c + 1,
            node.p * 2,
            node.s + 2,
            node.b,
            2,
          )
          if right.p <= right.s + K - right.c:
            if right.p >= right.s:
              k = right.p - right.s + right.c
              m = minimal_product_sums.get(k, right.p)
              if m >= right.p:
                minimal_product_sums[k] = right.p
              if k in ks:
                ks.remove(k)
            children.append(right)
    nodes = children
  return set(minimal_product_sums.values())

print(sum(minimal_product_sums(int(argv[1]))))
