while True :
  x, a, b = input().split()
  if x =='#' and a == '0' and b =='0' :
    break
  
  if int(a) > 17 or int(b) >= 80 :
    print(f'{x} Senior')
  else :
    print(f'{x} Junior')