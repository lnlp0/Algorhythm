n = int(input())

arr = []

for i in range(n) :
    N = int(input())
    if N == 0 :
        arr.pop()
    else :
        arr.append(N)

print(sum(arr))