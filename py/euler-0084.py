from sys import argv
from random import seed, randrange, shuffle
from time import time

squares = {
  'GO':    0,
  'A1':    1,
  'CC1':   2,
  'A2':    3,
  'T1':    4,
  'R1':    5,
  'B1':    6,
  'CH1':   7,
  'B2':    8,
  'B3':    9,
  'JAIL': 10,
  'C1':   11,
  'U1':   12,
  'C2':   13,
  'C3':   14,
  'R2':   15,
  'D1':   16,
  'CC2':  17,
  'D2':   18,
  'D3':   19,
  'FP':   20,
  'E1':   21,
  'CH2':  22,
  'E2':   23,
  'E3':   24,
  'R3':   25,
  'F1':   26,
  'F2':   27,
  'U2':   28,
  'F3':   29,
  'G2J':  30,
  'G1':   31,
  'G2':   32,
  'CC3':  33,
  'G3':   34,
  'R4':   35,
  'CH3':  36,
  'H1':   37,
  'T2':   38,
  'H2':   39,
}

def roll_dice(s):
  return (randrange(1, s + 1), randrange(1, s + 1))

def draw_community_chest(cards, square):
  card = cards.pop()
  cards.insert(0, card)
  if card == 0:
    return squares['GO']
  if card == 1:
    return squares['JAIL']
  return square

def draw_chance(cards, square):
  card = cards.pop()
  cards.insert(0, card)
  if card == 0:
    return squares['GO']
  if card == 1:
    return squares['JAIL']
  if card == 2:
    return squares['C1']
  if card == 3:
    return squares['E3']
  if card == 4:
    return squares['H2']
  if card == 5:
    return squares['R1']
  if card == 6 or card == 7:
    r = [k for k in squares.keys() if k[0] == 'R' and squares[k] > square]
    if len(r):
      return squares[r[0]]
    return squares['R1']
  if card == 8:
    u = [k for k in squares.keys() if k[0] == 'U' and squares[k] > square]
    if len(u):
      return squares[u[0]]
    return squares['U1']
  if card == 9:
    return (square - 3) % 40
  return square

def take_turn(community_chest, chance, sides, square, doubles=0):
  roll = roll_dice(sides)
  if roll[0] == roll[1]:
    doubles += 1
    if doubles == 3:
      return squares['JAIL'], 0
  else:
    doubles = 0
  square = (square + sum(roll)) % 40
  if square in (squares['CC1'], squares['CC2'], squares['CC3']):
    square = draw_community_chest(community_chest, square)
  elif square in (squares['CH1'], squares['CH2'], squares['CH3']):
    square = draw_chance(chance, square)
  elif square == squares['G2J']:
    square = squares['JAIL']
  return square, doubles
    
seed(time())
sides = int(argv[1])
community_chest = list(range(0, 16))
chance = list(range(0, 16))
shuffle(community_chest)
shuffle(chance)
state = (squares['GO'],)
freq = {state[0]: 1}
try:
  while 1:
    state = take_turn(community_chest, chance, sides, *state)
    freq[state[0]] = freq.get(state[0], 0) + 1
except KeyboardInterrupt:
  print()
s = list(reversed(sorted([(v, k) for k, v, in freq.items()])))[:3]
print(''.join(['%02d' % k for v, k in s]))
