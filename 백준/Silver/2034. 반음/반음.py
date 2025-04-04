num = int(input())
piano = ['C', 'X', 'D', 'X', 'E', 'F', 'X', 'G', 'X', 'A', 'X', 'B']
arr = []
for i in range(num):
  arr.append(int(input()))
  arr[i] %= 12

for i in range(65, 72):  #A부터 G까지 확인
  alpah = chr(i)
  idx = piano.index(alpah)
  success = True
  for j in arr:
    idx += j
    idx %= 12
    if piano[idx] == 'X':
      success = False
      break

  if success:
    print(f'{alpah} {piano[idx]}')