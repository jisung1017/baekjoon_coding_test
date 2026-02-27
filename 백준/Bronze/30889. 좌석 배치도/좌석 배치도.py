N = int(input())

A = [['.' for _ in range(20)] for _ in range(10)]
for _ in range(N) :
  x = input().strip()
  
  row_idx = ord(x[0]) - 65
  col_idx = int(x[1:]) - 1
  
  A[row_idx][col_idx] = 'o'
  
for row in A :
  print(''.join(row))