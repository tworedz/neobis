n, m = list(map(int,input().split()))
cnt = 0
flag = []
s = input()
s = s.split(' ')

aas = input()
aas = aas.split(' ')
a = set(aas[i] for i in range(len(aas)))
bbs = input()
bbs = bbs.split(' ')
b = set(bbs[i] for i in range(len(bbs)))
for i in range(n):
    ss = {s[i]}
    if ss.issubset(a):
        cnt= cnt + 1
    if ss.issubset(b):
        cnt= cnt - 1
print(cnt)
