import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
R, C = map(int, input().rstrip().split())

dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,1,-1,1,-1,0,1]
move_li = [(R, C)] + [(R+dr[i], C+dc[i]) for i in range(8) if 1<=R+dr[i]<=N and 1<=C+dc[i]<=N]
immove_set = set()

for i in range(K):
    R_i, C_i = map(int, input().rstrip().split())
    for mR, mC in move_li:
        if abs(mR-R_i) == abs(mC-C_i) or mR == R_i or mC == C_i:
            immove_set.add((mR, mC))

if (R,C) in immove_set:
    if len(move_li) == len(immove_set):
        print('CHECKMATE')
    else:
        print('CHECK')
else:
    if len(immove_set) == len(move_li)-1:
        print('STALEMATE')
    else:
        print('NONE')