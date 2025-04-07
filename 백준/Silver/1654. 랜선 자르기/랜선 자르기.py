import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lengths = [int(input()) for _ in range(k)]
max_length = max(lengths)
result = 0

def binary_search(low, high):
    global result
    while low <= high:
        mid = (low + high) // 2
        pieces = sum(length // mid for length in lengths)
        if pieces >= n:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

binary_search(1, max_length)
print(result)