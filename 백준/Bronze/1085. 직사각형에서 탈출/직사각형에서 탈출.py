x,y,w,h=map(int,input().split())
wi=0
hi=0
for a in range(w):
    if (x+a==w or x-a==w or x+a==0 or x-a==0):
        wi=a
        break
for b in range(h+1):
    if (y+b==h or y-b==h or y-b==0 or y+b==h):
        hi=b
        break
if (hi>wi):
    print(wi)
else:
    print(hi)