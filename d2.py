f = open("demofile.txt", "r")
r = 0
g = 0
b = 0
total = 0
game = 0
lst = []
no = False
for i in f:
  _, a = i.split(': ')
  a = a.replace(';', ',')
  lst = a.split(', ')
  game += 1
  r = 0
  g = 0
  b = 0
  for j in lst:
      z, y = j.split(' ')
      if 'd' in y:
        r = max(r, int(z))
      if 'b' in y:
        b = max(b, int(z))
      if 'g' in y:
        g = max(g,int(z))
  total += r*g*b
print(total)  
#Game 1: 19 blue, 12 red; 19 blue, 2 green, 1 red; 13 red, 11 blue