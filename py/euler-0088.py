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

  def __init__(self, n, l, p, s):
    self.n = n
    self.l = l
    self.p = p
    self.s = s

  def left_child(self):
    return Node(
      self.n[:-1] + (self.n[-1] + 1,),
      self.l,
      self.p + self.p // self.n[-1],
      self.s + 1,
    )

  def right_child(self):
    return Node(
      self.n[-1:] + (2,),
      self.l + 1,
      self.p * 2,
      self.s + 2,
    )

def minimal_product_sums(K):
  nodes = [Node((2,), 1, 2, 2)]
  minimal_product_sums = dict()
  ks = set(range(2, K + 1))
  while len(ks):
    parents, children, nodes = nodes, [], []
    for node in parents:
      if node.l == 1:
        nodes.append(node.left_child())
        children.append(node.right_child())
      else:
        if node.n[0] > node.n[1]:
          children.append(node.left_child())
        if node.l < K:
          children.append(node.right_child())
    for child in children:
      if child.p <= child.s + K - child.l:
        if child.p >= child.s:
          k = child.p - child.s + child.l
          m = minimal_product_sums.get(k, child.p)
          if m >= child.p:
            minimal_product_sums[k] = child.p
          if k in ks:
            ks.remove(k)
        nodes.append(child)
  return set(minimal_product_sums.values())

print(sum(minimal_product_sums(int(argv[1]))))
