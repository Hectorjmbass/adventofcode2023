with open("demofile.txt", "r") as fd:
  lines = [line.strip() for line in fd.readlines()]

def f(x, acc=0):
  return x[-1] + acc if not x or all(x[i + 1] - num == 0 for i, num in enumerate(x[:-1])) else f([x[i + 1] - num for i, num in enumerate(x[:-1])], x[-1] + acc)

total = 0
for i in lines:
  nums = [int(n) for n in i.split(' ')]
  nums = nums[::-1]
  total += f(nums)
print(total)
#1861775706
#1082