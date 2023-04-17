from itertools import combinations, permutations
from os import path

# Get cell value.
def get_cell(p, i, j):
  return p[j][i]

# Get all values in box (bi, bj).
def get_box(p, bi, bj):
  return [
    get_cell(p, 3 * bi + i, 3 * bj + j)
    for j in range(0, 3) for i in range(0, 3)
  ]

# Get all values in a column i.
def get_col(p, i):
  return [get_cell(p, i, j) for j in range(0, 9)]

# Get all values in a row j.
def get_row(p, j):
  return [get_cell(p, i, j) for i in range(0, 9)]

# Get value (i, j) from box (bi, bj).
def get_box_cell(p, bi, bj, i, j):
  return get_cell(p, 3 * bi + i, 3 * bj + j)

# Get column i from box (bi, bj).
def get_box_col(p, bi, bj, i):
  return [get_cell(p, 3 * bi + i, 3 * bj + j) for j in range(0, 3)]

# Get row j from box (bi, bj).
def get_box_row(p, bi, bj, j):
  return [get_cell(p, 3 * bi + i, 3 * bj + j) for i in range(0, 3)]

# Get column i overlapping box (bi).
def get_col_over_box(p, bi, i):
  return get_col(p, 3 * bi + i)

# Get row j overlapping box (bj).
def get_row_over_box(p, bj, j):
  return get_row(p, 3 * bj + j)

# Get cell j from column i overlapping box (bi).
def get_col_over_box_cell(p, bi, i, j):
  return get_col(p, 3 * bi + i)[j]

# Get cell i from row j overlapping box (bj).
def get_row_over_box_cell(p, bj, i, j):
  return get_row(p, 3 * bj + j)[i]

# Get all cells in the box containing cell (i, j).
def get_cell_box(p, i, j):
  return get_box(p, i // 3, j // 3)

# Return values that are subsets.
def subsets(values):
  return [s for s in values if type(s) == tuple]

# Set cell value (i, j) to v.
def set_cell(p, i, j, v):
  u = p[j][i]
  p[j][i] = v
  return u != v

# Set cell (i, j) in box (bi, bj) to v.
def set_box_cell(p, bi, bj, i, j, v):
  p[3 * bj + j][3 * bi + i] = v

# Set cell (i, j) in column overlapping box (bi) to v.
def set_col_over_box_cell(p, bi, i, j, v):
  p[j][3 * bi + i] = v

# Set cell (i, j) in row overlapping box (bj) to v.
def set_row_over_box_cell(p, bj, i, j, v):
  p[3 * bj + j][i] = v

# Get frequency map of values.
def freq(values):
  return dict(
    [(v, values.count(v)) for v in range(1, 10) if v in values]
    + [(v, 1) for s in values if type(s) == tuple for v in s]
  )

# Return True if n can be placed in cell value.
def is_placeable(v, n):
  return v == 0 or (type(v) == tuple and  n in v)

# Return the number of empty cells in values.
def count_placeable(values, n):
  return sum([1 for v in values if is_placeable(v, n)])

# Return True if cell value is solved.
def is_cell_solved(v):
  return not type(v) == tuple and v != 0

# Return True if box (bi, bj) is solved.
def is_box_solved(p, bi, bj):
  return all([is_cell_solved(v) for v in get_box(p, bi, bj)])

# Return True if column i is solved.
def is_col_solved(p, i):
  return all([is_cell_solved(v) for v in get_col(p, i)])

# Return True if row j is solved.
def is_row_solved(p, j):
  return all([is_cell_solved(v) for v in get_row(p, j)])

# Return True if column i overlapping box (bi, bj) is solved.
def is_col_over_box_solved(p, bi, i):
  return all([is_cell_solved(v) for v in get_col_over_box(p, bi, i)])

# Return True if row j is overlapping box (bi, bj) is solved.
def is_row_over_box_solved(p, bj, j):
  return all([is_cell_solved(v) for v in get_row_over_box(p, bj, j)])

# Return True if puzzle is solved.
def is_solved(p):
  for bi in range(0, 3):
    for bj in range(0, 3):
      if not is_box_solved(p, bi, bj):
        return False
  for i in range(0, 9):
    if not is_col_solved(p, i):
      return False
  for j in range(0, 9):
    if not is_row_solved(p, j):
      return False
  return True

# Return True if box (bi, bj) contains at most 1 occurrence of any values in
# the range(1, 10).
def is_box_well_formed(p, bi, bj):
  b = [n for n in get_box(p, bi, bj) if n != 0]
  return all([count == 1 for count in freq(b).values()])

# Return True if column i contains at most 1 occurrence of any values in the
# range(1, 10).
def is_col_well_formed(p, i):
  c = [n for n in get_col(p, i) if n != 0]
  return all([count == 1 for count in freq(c).values()])

# Return True if row j contains at most 1 occurrence of any values in the
# range(1, 10).
def is_row_well_formed(p, j):
  r = [n for n in get_row(p, j) if n != 0]
  return all([count == 1 for count in freq(r).values()])

# Return True if all boxes, columns, and rows contain at most 1 occurrence of
# any values in the range(1, 10).
def is_well_formed(p):
  for bi in range(0, 3):
    for bj in range(0, 3):
      if not is_box_well_formed(p, bi, bj):
        return False
  for i in range(0, 9):
    if not is_col_well_formed(p, i):
      return False
  for j in range(0, 9):
    if not is_row_well_formed(p, j):
      return False
  return True

# Scan for solvable cells among the columns in box(bi, bj).
def scan_box_cols(p, bi, bj, n):
  for i in range(0, 3):
    if not is_col_over_box_solved(p, bi, i):
      o = tuple(set(range(0, 3)) - set([i]))
      cn = freq(
        get_col_over_box(p, bi, o[0])
        + get_col_over_box(p, bi, o[1])
      ).get(n, 0)
      if cn == 2:
        # Found n in both of the other columns.
        bc = get_box_col(p, bi, bj, i)
        if bc.count(0) == 1:
          # Only 1 possibility to place n.
          set_box_cell(p, bi, bj, i, bc.index(0), n)
          return True
        # Find a row without n to place in.
        # Scan for a column without an n.
        cj = None
        for j in range(0, 3):
          if is_placeable(bc[j], n) \
             and freq(get_row_over_box(p, bj, j)).get(n, 0) == 0:
            if cj == None:
              cj = j
            else:
              cj = None
              break
        if cj != None:
          set_box_cell(p, bi, bj, i, cj, n)
          return True

# Scan for solvable cells among the rows in box(bi, bj).
def scan_box_rows(p, bi, bj, n):
  for j in range(0, 3):
    if not is_row_over_box_solved(p, bj, j):
      o = tuple(set(range(0, 3)) - set([j]))
      cn = freq(
        get_row_over_box(p, bj, o[0])
        + get_row_over_box(p, bj, o[1])
      ).get(n, 0)
      if cn == 2:
        # Found n in both of the other rows.
        br = get_box_row(p, bi, bj, j)
        if br.count(0) == 1:
          # Only 1 possibility to place n.
          set_box_cell(p, bi, bj, br.index(0), j, n)
          return True
        # Find a column without n to place in.
        # Scan for a row without an n.
        ci = None
        for i in range(0, 3):
          if is_placeable(br[i], n) \
             and freq(get_col_over_box(p, bi, i)).get(n, 0) == 0:
            if ci == None:
              ci = i
            else:
              ci = None
              break
        if ci != None:
          set_box_cell(p, bi, bj, ci, j, n)
          return True

# Scan for solvable cells in box (bi, bj).
def scan_box(p, bi, bj):
  b = set(get_box(p, bi, bj))
  for n in range(1, 10):
    if n not in b:
      if scan_box_cols(p, bi, bj, n) or scan_box_rows(p, bi, bj, n):
        continue

# Scan for solvable cells in puzzle.
def scan(p):
  for bi in range(0, 3):
    for bj in range(0, 3):
      if not is_box_solved(p, bi, bj):
        scan_box(p, bi, bj)

# Search for single candidates.
def search_single(p):
  for bi in range(0, 3):
    for bj in range(0, 3):
      if not is_box_solved(p, bi, bj):
        b = get_box(p, bi, bj)
        c, r = [None] * 3, [None] * 3
        for i in range(0, 3):
          if not is_col_over_box_solved(p, bi, i):
            c[i] = get_col_over_box(p, bi, i)
        for j in range(0, 3):
          if not is_row_over_box_solved(p, bj, j):
            r[j] = get_row_over_box(p, bj, j)
        for i in range(0, 3):
          for j in range(0, 3):
            if c[i] and r[j]:
              n = set(range(1, 10)) \
                - set(freq(c[i]).keys()) \
                - set(freq(r[j]).keys())
              v = get_box_cell(p, bi, bj, i, j)
              if v == 0 and len(n) == 1:
                n = list(n)[0]
              elif type(v) == tuple and len(n & set(v)) == 1:
                n = list(n & set(v))[0]
              else:
                n = None
              if n != None:
                set_box_cell(p, bi, bj, i, j, n)
                c[i][3 * bi + i] = n
                r[j][3 * bj + j] = n

# Solve cells in box by eliminating numbers from columns.
def eliminate_box_cols(p, bi, bj, n):
  for obj in set(range(0, 3)) - set([bj]):
    if freq(get_box(p, bi, obj)).get(n, 0) == 0:
      c = [v for j in range(0, 3) for v in get_row_over_box(p, obj, j)]
      if freq(c).get(n, 0) == 1:
        for j in range(0, 3):
          if freq(get_row_over_box(p, obj, j)).get(n, 0):
            oj = set(range(0, 3)) - set([j])
            r = [get_box_row(p, bi, obj, j) for j in oj]
            if count_placeable(r[0], n) == 1 and count_placeable(r[1], n) == 1:
              for i in range(0, 3):
                if is_placeable(r[0][i], n) and is_placeable(r[1][i], n):
                  # Box (bi, obj) must contain n in column i, therefore
                  # box (bi, bj) cannot contain n in column i.
                  ci = set(range(0, 3)) - set([i])
                  c = [get_box_col(p, bi, bj, i) for i in ci]
                  if count_placeable(c[0] + c[1], n) == 1:
                    # Box (bi, bj) has a single empty cell in its other columns,
                    # so n must be placed there.
                    for i in ci:
                      for j in range(0, 3):
                        if is_placeable(get_box_cell(p, bi, bj, i, j), n):
                          set_box_cell(p, bi, bj, i, j, n)
                          return True
            break

# Solve cells in box by eliminating numbers from rows.
def eliminate_box_rows(p, bi, bj, n):
  for obi in set(range(0, 3)) - set([bi]):
    if freq(get_box(p, obi, bj)).get(n, 0) == 0:
      c = [v for i in range(0, 3) for v in get_col_over_box(p, obi, i)]
      if freq(c).get(n, 0) == 1:
        for i in range(0, 3):
          if freq(get_col_over_box(p, i, obi)).get(n, 0):
            oi = set(range(0, 3)) - set([i])
            c = [get_box_col(p, obi, bj, i) for i in oi]
            if count_placeable(c[0], n) == 1 and count_placeable(c[1], n) == 1:
              for j in range(0, 3):
                if is_placeable(c[0][j], n) and is_placeable(c[1][j], n):
                  # Box (obi, bj) must contain n in row j, therefore
                  # box (bi, bj) cannot contain n in row j.
                  cj = set(range(0, 3)) - set([j])
                  r = [get_box_row(p, bi, bj, j) for j in cj]
                  if count_placeable(r[0] + r[1], n) == 1:
                    # Box (bi, bj) has a single empty cell in its other rows,
                    # so n must be placed there.
                    for j in cj:
                      for i in range(0, 3):
                        if is_placeable(get_box_cell(p, bi, bj, i, j), n):
                          set_box_cell(p, bi, bj, i, j, n)
                          return True
            break

# Solve cells in box by eliminating columns and rows.
def eliminate_box(p, bi, bj):
  b = set(get_box(p, bi, bj))
  for n in range(1, 10):
    if n not in b:
      if eliminate_box_cols(p, bi, bj, n) or eliminate_box_rows(p, bi, bj, n):
        continue

# Solve cells by eliminating columns and rows.
def eliminate(p):
  for bi in range(0, 3):
    for bj in range(0, 3):
      if not is_box_solved(p, bi, bj):
        eliminate_box(p, bi, bj)

# Solve cells by searching for missing numbers in columns.
def search_missing_col(p, i, n):
  cj = [j for j in range(0, 9) if is_placeable(get_cell(p, i, j), n)]
  tj = [j for j in cj if freq(get_row(p, j)).get(n, 0)]
  if len(cj) == len(tj) - 1:
    j = list(set(cj) - set(tj))[0]
    set_cell(p, i, j, n)

# Solve cells by searching for missing numbers in rows.
def search_missing_row(p, j, n):
  ci = [i for i in range(0, 9) if is_placeable(get_cell(p, i, j), n)]
  ti = [i for i in ci if freq(get_col(p, i)).get(n, 0)]
  if len(ci) == len(ti) - 1:
    j = list(set(cj) - set(tj))[0]
    set_cell(p, i, j, n)

# Solve cells by searching for missing numbers in columns and rows.
def search_missing(p):
  for i in range(0, 9):
    if not is_col_solved(p, i):
      for n in range(1, 10):
        if freq(get_col(p, i)).get(n, 0) == 0:
          search_missing_col(p, i, n)
  for j in range(0, 9):
    if not is_row_solved(p, j):
      for n in range(1, 10):
        if freq(get_row(p, j)).get(n, 0) == 0:
          search_missing_row(p, j, n)

# Add disjoint subsets in place of unsolved cells.
def find_disjoint_subsets(p):
  for bi in range(0, 3):
    for bj in range(0, 3):
      if not is_box_solved(p, bi, bj):
        b = set(get_box(p, bi, bj))
        for i in range(0, 3):
          for j in range(0, 3):
            if get_box_cell(p, bi, bj, i, j) == 0:
              set_box_cell(p, bi, bj, i, j, tuple(
                set(range(1, 10)) \
                - b \
                - set(get_col_over_box(p, bi, i)) \
                - set(get_row_over_box(p, bj, j))
              ))

# Return a copy of the puzzle with unsolved cells in place of disjoint subsets.
def remove_disjoint_subsets(p):
  for i in range(0, 9):
    for j in range(0, 9):
      v = get_cell(p, i, j)
      if type(v) == tuple:
        set_cell(p, i, j, 0)

# Return hidden pairs among values.
def hidden_pairs(values):
  pairs = []
  for c in combinations(range(0, len(values)), 2):
    i, j = c
    if type(values[i]) == tuple and type(values[j]) == tuple:
      u = set(values[i]) & set(values[j])
      o = set()
      for k in set(range(0, len(values))) - set(c):
        if type(values[k]) == tuple:
          o |= set(values[k])
      h = u - o
      if len(h) == 2 and len(o - h) == len(o):
        pairs.append(tuple(h))
  return pairs

# Return value less subset, or a solved value if only one value remains.
def remove_subset(subset, value):
  if type(value) == tuple:
    u = set(value) - subset
    if len(u) == 1:
      return list(u)[0]
  return value

def set_col_pair(p, i, pair):
  for j in range(0, 9):
    v = get_cell(p, i, j)
    if type(v) == tuple:
      if len(set(v) & set(pair)) == 2:
        set_cell(p, i, j, pair)

def set_row_pair(p, j, pair):
  for i in range(0, 9):
    v = get_cell(p, i, j)
    if type(v) == tuple:
      if len(set(v) & set(pair)) == 2:
        set_cell(p, i, j, pair)

def set_box_pair(p, bi, bj, pair):
  for i in range(0, 3):
    for j in range(0, 3):
      v = get_box_cell(p, bi, bj, i, j)
      if type(v) == tuple:
        if len(set(v) & set(pair)) == 2:
          set_box_cell(p, bi, bj, i, j, pair)

def set_pairs(p):
  for bi in range(0, 3):
    for bj in range(0, 3):
      for pair in hidden_pairs(get_box(p, bi, bj)):
        set_box_pair(p, bi, bj, pair)
  for i in range(0, 9):
    for pair in hidden_pairs(get_col(p, i)):
      set_col_pair(p, i, pair)
  for j in range(0, 9):
    for pair in hidden_pairs(get_row(p, j)):
      set_row_pair(p, j, pair)

def naked_pairs(values):
  pairs = [pair for pair in values if type(pair) == tuple and len(pair) == 2]
  f = dict()
  for pair in pairs:
    f[pair] = f.get(pair, 0) + 1
  return [pair for pair, count in f.items() if count == 2]

def scan_pairs(p):
  for i in range(0, 9):
    col_pairs = naked_pairs(get_col(p, i))
    for j in range(0, 9):
      v = get_cell(p, i, j)
      for pair in col_pairs:
        if set_cell(p, i, j, remove_subset(set(pair), v)):
          return True
      for pair in naked_pairs(get_row(p, j)):
        if set_cell(p, i, j, remove_subset(set(pair), v)):
          return True
      for pair in naked_pairs(get_cell_box(p, i, j)):
        if set_cell(p, i, j, remove_subset(set(pair), v)):
          return True

def eliminate_subsets(p, i, j, values):
  v = get_cell(p, i, j)
  if type(v) == tuple:
    u = subsets(values)
    k = u.index(v)
    u = u[:k] + u[k + 1:]
    if set_cell(p, i, j, remove_subset(set([n for s in u for n in s]), v)):
      return True

def scan_subsets(p):
  for i in range(0, 9):
    for j in range(0, 9):
      if eliminate_subsets(p, i, j, get_col(p, i)):
        return True
      if eliminate_subsets(p, i, j, get_row(p, j)):
        return True
      if eliminate_subsets(p, i, j, get_cell_box(p, i, j)):
        return True

def scan_xwings(p):
  for i1, i2 in combinations(range(0, 9), 2):
    for j1, j2 in combinations(range(0, 9), 2):
      a = get_cell(p, i1, j1)
      b = get_cell(p, i2, j1)
      c = get_cell(p, i1, j2)
      d = get_cell(p, i2, j2)
      if type(a) == tuple and type(b) == tuple \
         and type(c) == tuple and type(d) == tuple:
        x = set(a) & set(b)
        y = set(c) & set(d)
        if len(x) == 1 and x == y:
          v = list(x)[0]
          ci = set(range(0, 9)) - set([i1, i2])
          r1 = set()
          for s in subsets([get_cell(p, i, j1) for i in ci]):
            r1 |= set(s)
          r2 = set()
          for s in subsets([get_cell(p, i, j2) for i in ci]):
            r2 |= set(s)
          if v not in r1 and v not in r2:
            rj = set(range(0, 9)) - set([j1, j2])
            m = False
            for j in rj:
              m |= set_cell(p, i1, j, remove_subset(x, get_cell(p, i1, j)))
              m |= set_cell(p, i2, j, remove_subset(x, get_cell(p, i2, j)))
            return m

def solve_subsets(p):
  find_disjoint_subsets(p)
  set_pairs(p)
  if not is_well_formed:
    return False
  if scan_subsets(p):
    remove_disjoint_subsets(p)
    return True
  scan_xwings(p)
  if not is_well_formed:
    return False
  if scan_subsets(p):
    remove_disjoint_subsets(p)
    return True
  remove_disjoint_subsets(p)

# Return a deep copy of a puzzle.
def copy(p):
  return [r.copy() for r in p]

# Returns True if f(p) mutates p.
def mutates(f, p):
  q = copy(p)
  f(p)
  return any([tuple(r) != tuple(s) for r, s in zip(p, q)])

def get_values(values):
  if len(values) == 0:
    yield []
  else:
    for n in values[0]:
      for o in get_values(values[1:]):
        yield [n] + o

def fuzz(p):
  unsolved_cells = []
  for i in range(0, 9):
    for j in range(0, 9):
      if get_cell(p, i, j) == 0:
        unsolved_cells.append((i, j))
  count = 1
  while 1:
    q = copy(p)
    find_disjoint_subsets(q)
    for cells in combinations(unsolved_cells, count):
      for values in get_values([get_cell(q, i, j) for i, j in cells]):
        r = copy(q)
        remove_disjoint_subsets(r)
        for ind in range(0, count):
          i, j = cells[ind]
          set_cell(r, i, j, values[ind])
        yield r
    count += 1

def solve(p):
  m = True
  while m:
    m = True
    while m:
      m = False
      if is_solved(p):
        return True
      m |= mutates(scan, p)
      if is_solved(p):
        return True
      if not is_well_formed(p):
        return False
      m |= mutates(search_single, p)
      if is_solved(p):
        return True
      if not is_well_formed(p):
        return False
      m |= mutates(eliminate, p)
      if is_solved(p):
        return True
      if not is_well_formed(p):
        return False
      m |= mutates(search_missing, p)
      if is_solved(p):
        return True
      if not is_well_formed(p):
        return False
    if is_well_formed(p):
      m |= mutates(solve_subsets, p)
      if is_solved(p):
        return True
      if not is_well_formed(p):
        return False
  guess = fuzz(p)
  while not solve(q := next(guess)):
    pass
  for j in range(0, 9):
    p[j] = q[j]
  return True

f = open(path.join(path.dirname(__file__), '../resources/p096_sudoku.txt'))
m = [l.strip() for l in f if not l.startswith('Grid')]
p = [
  [
    [int(c) for c in r] for r in m[9 * i:9 * i + 9]
  ] for i in range(0, len(m) // 9)
]

s = 0
for i in range(0, len(p)):
  solve(p[i])
  x = get_row(p[i], 0)[:3]
  s += x[0] * 100 + x[1] * 10 + x[2]
print(s)
