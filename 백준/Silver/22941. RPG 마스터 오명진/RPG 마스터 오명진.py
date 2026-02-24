import sys
input = sys.stdin.readline 
from math import ceil

b_hp, b_atk, d_hp, d_atk = map(int, input().split())
p,s = map(int, input().split())
b_death = ceil(b_hp/d_atk)
d_death = ceil(d_hp/b_atk) if (d_hp-p) % b_atk and (d_hp-p) % b_atk + p <= b_atk else ceil((d_hp+s)/b_atk)
if b_death >= d_death:
    print('Victory!')
else:
    print('gg')