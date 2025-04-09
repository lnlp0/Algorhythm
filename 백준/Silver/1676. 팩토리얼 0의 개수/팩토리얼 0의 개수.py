c = 0
fac = 1
a = int(input())
for i in range(1,a+1):
    fac *= i
fac = str(fac)
for i in range(len(fac)-1,-1,-1):
    if fac[i] == "0":
        c+=1
    else:
        print(c)
        break
