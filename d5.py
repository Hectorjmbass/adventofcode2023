with open("demofile.txt", "r") as fd:
  lines = list(map(lambda x: x.strip(), fd.readlines()))
_, inputs = lines[0].split(': ')
inputs = list(map(int, inputs.split(' ')))
seeds = []

for i in range(0, len(inputs), 2):
  seeds.append((inputs[i], inputs[i]+inputs[i+1]))


chunkered = []
def chunker(lst, ini=-1):
  match lst, ini:
      case [], result:
          return result
      case [first, *rest], x:
          chunkered.append(lines[x+2:first])
          return chunker(rest, first)

chunks = [pos for pos, char in enumerate(lines) if char == '']
chunker(chunks)
del chunkered[0]

for i in chunkered:
  ranges = []
  for j in i:
    ranges.append(list(map(int, j.split())))
  new = []
  while len(seeds) > 0:
    s, r = seeds.pop()
    for source, destination, range_ in ranges:
      os = max(s, destination)
      oe = min(r, destination + range_)
      if os < oe:
        new.append((os - destination + source, oe - destination + source))
        if os > s:
          seeds.append((s, os))
        if r > oe:
          seeds.append((oe, r))
        break
    else:
        new.append((s, r))
  seeds = new
print(min(seeds)[0])

#lines 29 to 42 needed external help to get the logic correct see HyperNeutrino
