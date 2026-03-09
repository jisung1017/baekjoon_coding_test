N = int(input())
date = [0] * 31

for _ in range(N) :
    s, e = map(int,input().split())
    for i in range(s,e) :
        date[i] += 1

K = int(input())

res = True
for x in date :
    if x > K :
        res = False

if res :
    print(1)
else :
    print(0)