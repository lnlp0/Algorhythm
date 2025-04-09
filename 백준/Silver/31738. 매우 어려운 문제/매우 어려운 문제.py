def factmod(n, m):
    if m == 1:
        return 0
    if n >= m:
        return 0
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % m

    return res


n, m = map(int, input().split())
print(factmod(n, m))