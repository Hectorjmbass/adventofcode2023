import math
from functools import reduce
with open("demofile.txt", "r") as fd:
  lines = [line.strip() for line in fd.readlines()]
direction = list(lines[0])
for a, b in enumerate(direction):
  if b == 'L':
    direction[a] = 0
  else:
    direction[a] = 1
counter = 0
starting = []
dict = {}
for i in lines[1:]:
  a, b = i.split(' = ')
  dict[a] = tuple(b.strip('()').split(', '))
  if i[2] == 'A':
    starting.append(a)

lst = []
for j in starting:
  current = j
  while True:
    for i in direction:
      current = dict[current][i]
      counter += 1
    if current[2] == 'Z':
      print(current)
      break

  lst.append(counter) 
  counter = 0
print(lst)
print(reduce(lambda x, y: x * y // math.gcd(x, y), lst))