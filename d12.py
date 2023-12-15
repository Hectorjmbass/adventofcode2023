import time
from functools import lru_cache

with open("demofile.txt", "r") as fd:
    lines = [line.strip() for line in fd.readlines()]

@lru_cache(maxsize=None)
def f(s, k, c=0):  
    if sum(k) < s.count('#') + c:
        return 0
    if sum(k) > s.count('#') + s.count('?') + c:
        return 0
    if len(k) == 0:
        if c == 0 and '#' not in s:
            return 1
        else:
            return 0
    if k[0] < c:
        return 0
    if s == '':
        return 0 
    if s[0] == '.':
        if c == k[0]:
            return f(s[1:], k[1:], 0)
        elif c == 0:
            return f(s[1:], k, 0)
        else:
            return 0
    if s[0] == '#':
        return f(s[1:], k, c+1)
    if s[0] == '?':
        return f('.'+s[1:], k, c) + f('#'+s[1:], k, c)
    print('error')
    exit(0)

start_time = time.time()

total = 0
for line in lines:
    a, b = line.split(' ')
    b = tuple([int(n) for n in b.split(',')]*5)
    total += f((a+'?')*4+a+'.', b)

end_time = time.time()

print(f"Total ways: {total}")
print(f"Execution time: {end_time - start_time} seconds")