import sys
sys.setrecursionlimit(10**7)

pre = []
for line in sys.stdin:
    line = line.strip()
    if not line: 
        continue
    pre.append(int(line))

i = 0
n = len(pre)
out = []

def build(low, high):
    global i
    if i >= n:
        return
    val = pre[i]
    # 현재 서브트리에 들어갈 수 없는 값이면 리턴
    if not (low < val < high):
        return
    i += 1             # 이 값을 소비하고
    build(low, val)    # 왼쪽 서브트리 구성
    build(val, high)   # 오른쪽 서브트리 구성
    out.append(val)    # 좌/우 처리 후 루트를 추가 → 후위

build(float('-inf'), float('inf'))
print("\n".join(map(str, out)))