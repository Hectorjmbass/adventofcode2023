import time
from functools import lru_cache

with open("demofile.txt", "r") as fd:
  grid = fd.read().split('\n')
lines = [list(a) for a in grid]



@lru_cache(maxsize=None)
def tilt(lines: tuple[tuple[str]], d):
  lines = [list(row) for row in lines]
  if d == 'north':  
    result = north(lines)
  if d == 'west':
    result = west(lines)
  if d == 'south':
    result = south(lines)
  if d == 'east':
    result = east(lines)
  return tuple(tuple(row) for row in result)

def north(lines: list[list[str]]):
  flag = True
  while flag:
    flag = False
    for a in range(len(lines[0])):
      for b in range(1, len(lines)):
        if lines[b][a] == 'O' and lines[b-1][a] == '.':
          lines[b][a] = '.'
          lines[b-1][a] = 'O'
          flag = True
  return lines

def west(lines):
  flag = True
  while flag:
    flag = False
    for a in range(len(lines[0])-1):
      for b in range(len(lines)):
        if lines[b][a] == 'O' and lines[b][a+1] == '.':
          lines[b][a] = '.'
          lines[b][a+1] = 'O'
          flag = True
  return lines

def south(lines):
  flag = True
  while flag:
    flag = False
    for a in range(len(lines[0])):
      for b in range(len(lines)-1):
        if lines[b][a] == 'O' and lines[b+1][a] == '.':
          lines[b][a] = '.'
          lines[b+1][a] = 'O'
          flag = True
  return lines
start_time = time.time()

def east(lines):
  flag = True
  while flag:
    flag = False
    for a in range(1, len(lines[0])):
      for b in range(len(lines)):
        if lines[b][a] == 'O' and lines[b][a-1] == '.':
          lines[b][a] = '.'
          lines[b][a-1] = 'O'
          flag = True
  return lines
dict = {}
for i in range():
  lines = tilt(tuple(map(tuple, lines)), 'north')
  lines = tilt(tuple(map(tuple, lines)), 'west')
  lines = tilt(tuple(map(tuple, lines)), 'south')
  lines = tilt(tuple(map(tuple, lines)), 'east')


total = 0
for k ,i in enumerate(lines):  
  total += i.count('O')*(len(lines)-k)
print(total)

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")