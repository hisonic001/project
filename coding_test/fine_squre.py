from math import gcd
w,h = 8,12
if w>h:
    w,h = h,w

print(w*h-(h+w - gcd(w,h)))
