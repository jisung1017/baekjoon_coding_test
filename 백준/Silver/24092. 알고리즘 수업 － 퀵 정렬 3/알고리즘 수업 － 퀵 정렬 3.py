import sys

# 재귀 깊이 제한 설정
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    

    diff_count = 0
    for i in range(n):
        if a[i] != b[i]:
            diff_count += 1
            

    if diff_count == 0:
        print(1)
        exit()

    def swap(i, j):
        nonlocal diff_count

        if a[i] == b[i]: diff_count += 1
        a[i], a[j] = a[j], a[i]
        if a[i] == b[i]: diff_count -= 1
        

        if i != j:
            if a[j] == b[j]: diff_count += 1
            if a[j] == b[j]: diff_count -= 1 

    def update_and_swap(i, j):
        nonlocal diff_count
        for idx in [i, j]:
            if a[idx] == b[idx]: diff_count += 1
        
        a[i], a[j] = a[j], a[i]
        
        for idx in [i, j]:
            if a[idx] == b[idx]: diff_count -= 1
            
        if diff_count == 0:
            print(1)
            exit()

    def quick_sort(p, r):
        if p < r:
            q = partition(p, r)
            quick_sort(p, q - 1)
            quick_sort(q + 1, r)

    def partition(p, r):
        x = a[r]
        i = p - 1
        for j in range(p, r):
            if a[j] <= x:
                i += 1
                update_and_swap(i, j)
        if i + 1 != r:
            update_and_swap(i + 1, r)
        return i + 1

    quick_sort(0, n - 1)
    print(0)

if __name__ == '__main__' :
  solve()