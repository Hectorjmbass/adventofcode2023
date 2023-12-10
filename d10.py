with open("demofile.txt", "r") as fd:
  lines = [line.strip() for line in fd.readlines()]
counter = 0
for y, i in enumerate(lines):
  if 'S' in i:
    s = i.find('S'), y
    break

def pipes(x, y, type, last=None):
    if type == '-':
        a, b = (x-1, y), (x+1, y)
    elif type == '|':
        a, b = (x, y-1), (x, y+1)
    elif type == 'L':
        a, b = (x, y-1), (x+1, y)
    elif type == 'J':
        a, b = (x-1, y), (x, y-1)
    elif type == '7':
        a, b = (x, y+1), (x-1, y)
    elif type == 'F':
        a, b = (x, y+1), (x+1, y)
    else:
        return None
    if a != last:
        return a
    else:
        return b

lsts = []
lst = []
a = None
type = '-'
counter = 0
b = s
a = (35, 128)
lst = [s]
while True:
    counter += 1
    coord = pipes(*b, type, a)
    lst.append(coord)
    x, y = coord[0], coord[1]
    type = lines[y][x]
    a = b
    b = coord
    if type == 'S':
        break
print(counter//2)

#Used some code for part 2 from duckyluuk
#I was very stuck
def shoelace_area(points):
  n = len(points)
  res = 0
  for i in range(n):
    x1, y1 = points[i][0], points[i][1]
    x2, y2 = points[(i + 1) % n]
    res += x1 * y2 - x2 * y1
  return abs(res) >> 1

print(shoelace_area(lst)-counter//2+1)

