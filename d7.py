with open("demofile.txt", "r") as fd:
  lines = [line.strip() for line in fd.readlines()]

def eval_hand(hand, jokers):
  if jokers > 1 or hand[0] > 3:
      return hand[0] * 10 + jokers * 10
  elif hand == [3, 2]:
      return 32 if jokers == 0 else 40
  elif hand[0] == 2 and hand[1] == 2:
      return 22 if jokers == 0 else 32
  return hand[0] * 10 + jokers * 10

value = {}
bid_dict = {}
for line in lines:
  cards, bid = line.split(' ')
  bid_dict[cards] = bid
for cards in bid_dict.keys():
  if cards != 'JJJJJ':
      jokerless = cards.replace('J', '')
      hand = sorted([jokerless.count(letter) for letter in set(jokerless)], reverse=True)
      joker = cards.count('J')
      value[cards] = eval_hand(hand, joker)
  else:
      value[cards] = 50
sorted_cards = sorted(value.keys(), key=lambda x: (value[x], ['J23456789TQKA'.index(c) for c in x]), reverse=True)
total = sum(int(bid_dict[card]) * (len(lines) - i) for i, card in enumerate(sorted_cards))
print(total)