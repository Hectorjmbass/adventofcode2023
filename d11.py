with open("demofile.txt", "r") as fd:
  lines = [line.strip() for line in fd.readlines()]

row = []
column = list(range(len(lines)))
for x, z in enumerate(lines):
  if '#' not in z:
    row.append(x)
  for w, y in enumerate(z):
    if y == '#' and w in column:
      column.remove(w)

row.sort(reverse=True)
column.sort(reverse=True)

coords = []
for y, i in enumerate(lines):
  for x, j in enumerate(i):
    if j == '#':
      coords.append((x, y))

expansion = 1000000 - 1
total = 0
space = 0
for z, i in enumerate(coords):
  for j in coords[z+1:]:
    for x in column:
      if max(i[0], j[0]) >= x >= min(i[0], j[0]):
        total += 999999
    xd = max(i[0], j[0]) - min(i[0], j[0])
    for y in row:
      if max(i[1], j[1]) >= y >= min(i[1], j[1]):
        total += 999999
    yd = max(i[1], j[1]) - min(i[1], j[1])
    total += xd + yd
print(total)
#613686987427