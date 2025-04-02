n = int(input())
cards = list(map(int, input().split()))

cnt = {}
for c in cards:
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1

m = int(input())
nums = list(map(int, input().split()))

ans = []
for num in nums:
    if num in cnt:
        ans.append(str(cnt[num]))
    else:
        ans.append('0')

print(' '.join(ans))