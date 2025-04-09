import sys
input = sys.stdin.readline

c=0
a = int(input())
b = list(range(a))

for i in range(a):
    b[i] = int(input())
b.sort()
for i in range(a):
    print(b[i])