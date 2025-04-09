n = []
m = []
for _ in range(3):
    n.append(int(input()))
for _ in range(2):
    m.append(int(input()))

print(min(n)+min(m)-50)