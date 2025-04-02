import sys

def num(val):
  if val - int(val) >= 0.5:
    return int(val)+1
  else:
    return int(val)

n = int(sys.stdin.readline().strip())
if n:
  level = []
  for _ in range(n):
    level.append(int(sys.stdin.readline().strip()))

  nn = num(n * 0.15)
  level.sort()
  if nn > 0:
    print(num(sum(level[nn:-nn]) / len(level[nn:-nn])))
  else:
    print(num(sum(level) / len(level)))
else:
  print(0)