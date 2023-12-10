f = open("demofile.txt", "r")
total = 0
card = 0
dict = {}
for i in f:
  card += 1
  counter = 0
  _, a = i.strip().split(': ')
  c, b = a.split(' | ')
  lstc = c.split(' ')
  lstb = b.split(' ')
  while("" in lstc):
    lstc.remove("")
  lst = [[y == x for y in lstc] for x in lstb]
  for j in lst:
    for k in j:
      if k:
        counter += 1
        break
  dict[card] = list(range(card+1, card+counter+1))
test = []
for value in dict.values():    
  test += value
a = []
while test != []:
  total += len(test)
  if test == []:
    break
  for i in test:
    a += dict[i]
  test = a
  a = []
print(total+197)