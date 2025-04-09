num=int(input())
a,b=0,1
for i in range(1,num):
    a,b = b,a+b
print(a,b)