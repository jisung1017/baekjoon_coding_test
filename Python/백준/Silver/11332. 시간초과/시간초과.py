import sys
input = sys.stdin.readline
import math

for _ in range(int(input())) :
    A = list(map(str, input().split()))
    a = A[0]
    N, T, L = int(A[1]), int(A[2]), int(A[3]) * 10**8

    if a == 'O(N)' :   
        if N * T <= L :
            print('May Pass.')
        else :
            print('TLE!')
    elif a == 'O(N^2)' :
        if N **2 * T <= L :
            print('May Pass.')
        else :
            print('TLE!')
    elif a == 'O(N^3)' :
        if N **3 * T <= L :
            print('May Pass.')
        else :
            print('TLE!')
    elif a == 'O(2^N)' :
        if 2 **N * T <= L :
            print('May Pass.')
        else :
            print('TLE!')
    elif a == 'O(N!)' :
        if math.factorial(N) * T <= L :
            print('May Pass.')
        else :
            print('TLE!')