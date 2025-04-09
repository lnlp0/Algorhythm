a = int(input())
for i in range(1,100000):
    a-=i
    if a<0:
        print(i-1)
        break