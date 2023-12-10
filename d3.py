import fuckit
with open("demofile.txt", "r") as fd:
    lines = fd.readlines()
def neighbouring(x, y):
    matrix = [(xc, yc) for xc, yc in 
              [(x-1, y-1), (x, y-1), (x+1, y-1),
               (x-1, y), (x+1,y),
               (x-1, y+1), (x, y+1), (x+1, y+1)] 
              if xc >= 0 and yc >= 0]
    with fuckit:
      positions = [(xc, yc) for xc, yc in matrix if lines[xc][yc] == '*']
      return positions[0] if positions[0] else None
total = 0
num = ''
gears = {}
positions = None
for x, line in enumerate(lines):
    line = line.strip()
    for y, char in enumerate(line):
      if char.isnumeric():
        num += char
        if positions is None:
          positions = neighbouring(x, y)
      elif not char.isnumeric() and num:
        if positions is not None:
          print(num)
          if positions not in gears.keys():
            gears[positions] = int(num)
          else:
            total += int(num)*gears[positions]
            del gears[positions]
          positions = None
        num = ''
print(total)
#P.S. needs a layer of padding at the bottom ¯\_(ツ)_/¯