arr = []
for i in range(3):
    arr.append(int(input()))
if sum(arr) <= 21:
    print(1)
else:
    print(0)