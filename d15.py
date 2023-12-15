with open("demofile.txt", "r") as fd:
  lines = fd.read().split(',')

#sum = 0
#for i in lines:
  #total = 0
  #for j in i:
    #total = ((total + ord(j)) * 17) % 256
  #sum += total
#print(sum)

lst = [[] for _ in range(256)]

for step in lines:
  total = 0
  match step.strip('-').split('='):
    case [l, f]: 
      for i in l:
        total = ((total + ord(i)) * 17) % 256
      for k, i in enumerate(lst[total]):
        if i[0] == l:
          lst[total][k] = (l, f)
          break
      else:
        lst[total].append((l, f))
    case [l]:    
      for i in l:
        total = ((total + ord(i)) * 17) % 256
      for i in lst[total]:
        if i[0] == l:
          lst[total].remove(i)

sum = 0
for a, i in enumerate(lst):
  if i != []:
    for j, k in enumerate(i):
      sum += (j + 1) * int(k[1]) * (a + 1)
print(sum)