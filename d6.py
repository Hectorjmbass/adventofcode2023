with open("demofile.txt", "r") as fd:
  lines = list(map(lambda x: x.strip(), fd.readlines()))
_, time = lines[0].split(': ')
_, distance = lines[1].split(': ')
time = list(map(int, time.split(' ')))
distance = list(map(int, distance.split(' ')))
print(time)
print(distance)
total = 1
for i, j in enumerate(time):
  counter = 0
  for k in range(j, 0, -1):
    if (j-k)*k > distance[i]:
      counter += 1
  total *= counter
print(total)