d=int(input())
a = 0
b = 1
c = 0
if d==1:
    print(b)
else:
    for i in range(d-1):
        c = a+b
        a = b
        b = c
    print(c)
