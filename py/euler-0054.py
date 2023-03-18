from functools import total_ordering
from enum import Enum
from os import path

@total_ordering
class Hand(Enum):
  HIGH_CARD = 0
  PAIR = 1
  TWO_PAIR = 2
  THREE_OF_A_KIND = 3
  STRAIGHT = 4
  FLUSH = 5
  FULL_HOUSE = 6
  FOUR_OF_A_KIND = 7
  STRAIGHT_FLUSH = 8
  ROYAL_FLUSH = 9

  def __lt__(self, other):
    return self.value < other.value

class Card:

  value_map = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
  }

  def __init__(self, value, suit):
    self.value = value
    self.suit = suit

  def parse(card):
    return Card(Card.value_map[card[0]], card[1])

# Parse a string of cards into a (Hand, [values...]) tuple.
def parse_hand(cards):
  value_freq_map = dict()
  suit_freq_map = dict()
  for card in sorted(
      map(Card.parse, cards.split(' ')),
      key=lambda card: card.value,
  ):
    value_freq_map[card.value] = value_freq_map.get(card.value, 0) + 1
    suit_freq_map[card.suit] = suit_freq_map.get(card.value, 0) + 1
  values = list(reversed(value_freq_map.keys()))
  if values == list(reversed(range(values[0] - 4, values[0] + 1))):
    if len(suit_freq_map) == 1:
      if values[0] == value_map['A']:
        return (Hand.ROYAL_FLUSH,)
      return tuple([Hand.STRAIGHT_FLUSH] + values)
    return tuple([Hand.STRAIGHT] + values)
  if 4 in value_freq_map.values():
    value = next(filter(
      lambda value: value_freq_map[value] == 4,
      value_freq_map,
    ))
    return tuple(
      [Hand.FOUR_OF_A_KIND, value]
      + [v for v in value_freq_map if value != v]
    )
  if 3 in value_freq_map.values() and 2 in value_freq_map.values():
    triplet = next(filter(
      lambda value: value_freq_map[value] == 3,
      value_freq_map,
    ))
    pair = next(filter(
      lambda value: value_freq_map[value] == 3,
      value_freq_map,
    ))
    return tuple([Hand.FULL_HOUSE, triplet, pair])
  if len(suit_freq_map) == 1:
    return tuple([Hand.FLUSH] + values)
  if 3 in value_freq_map.values():
    value = next(filter(
      lambda value: value_freq_map[value] == 3,
      value_freq_map,
    ))
    high_cards = list(reversed(sorted(
      [v for v in value_freq_map if value != v]
    )))
    return tuple([Hand.THREE_OF_A_KIND, value] + high_cards)
  if len([freq for freq in value_freq_map.values() if freq == 2]) == 2:
    pairs = list(reversed(sorted(
      [value for value in value_freq_map if value_freq_map[value] == 2]
    )))
    high_cards = list(reversed(sorted(
      [v for v in value_freq_map if v not in pairs]
    )))
    return tuple([Hand.TWO_PAIR] + pairs + high_cards)
  if 2 in value_freq_map.values():
    value = next(filter(
      lambda value: value_freq_map[value] == 2,
      value_freq_map,
    ))
    high_cards = list(reversed(sorted(
      [v for v in value_freq_map if value != v]
    )))
    return tuple([Hand.PAIR, value] + high_cards)
  return tuple([Hand.HIGH_CARD] + values)

f = open(path.join(path.dirname(__file__), '../resources/p054_poker.txt'))
hands = []
while True:
  l = f.readline()
  if not l:
    break
  hands.append(l.strip())
print(sum([parse_hand(hands[:14]) > parse_hand(hands[15:]) for hands in hands]))
