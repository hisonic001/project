# from bisect import bisect_left, bisect_right
#
# a =[1,2,4,4,8]
# x =4
# print(bisect_left(a,1.5))
# print(bisect_right(a,x))
#
# n,m = 4,6
# h = [19,15,10,17]
# h = sorted(h)
# cut = h[-1]-1
# def ricecake (array, cut, m):
#     rest=0
#     for i in range(len(array)):
#         if cut>=array[i]:
#             continue
#         else:
#             rest += array[i]-cut
#     if rest>m:
#         ricecake(array,cut+1,m)
#     elif rest<m:
#         ricecake(array,cut-1,m)
#     elif rest == m:
#         print(cut)
# ricecake(h,cut,m)
#

from bisect import bisect_left, bisect_right
array = [1,1,2,2,2,2,3]
x = 2
left = bisect_left(array,x)
right = bisect_right(array,x)
if right-left >0 : print(right-left)
else : print(-1)
