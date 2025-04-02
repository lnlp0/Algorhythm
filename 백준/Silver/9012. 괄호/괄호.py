num = int(input())

for i in range(num):
    arr = str(input())
    stack = 0
    is_vps = True

    for j in range(len(arr)):
        if arr[j] == "(":
            stack += 1
        elif arr[j] == ")":
            stack -= 1

        if stack < 0:
            is_vps = False
            break

    if stack != 0:
        is_vps = False

    if is_vps:
        print("YES")
    else:
        print("NO")