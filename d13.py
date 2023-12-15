import time
start_time = time.time()

with open("demofile.txt", "r") as fd:
  parts = list(map(str.split, fd.read().split('\n\n')))

def f(x):
  for i in range(len(x)):
      reversed_substrings = zip(x[i-1::-1], x[i:])
      character_pairs = (zip(l, m) for l, m in reversed_substrings)
      condition_sum = sum(c != d for pair in character_pairs for c, d in pair)

      if condition_sum == s:
          return i
  else:
      return 0

for s in 0, 1:
  result_sum = sum(100 * f(p) + f([*zip(*p)]) for p in parts)
print(result_sum)
end_time = time.time()