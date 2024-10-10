import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    a.append(sys.stdin.readline().strip())
b = set(a)
a = list(b)
a.sort()
a.sort(key = len)

for i in a:
    print(i)