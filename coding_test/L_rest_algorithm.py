# def find_parent(parent,x):
#     if parent[x] != x:
#         parent[x] = find_parnet(parent,parnet[x])
#     return parent[x]
#
# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b= find_parent(parent,b)
#     if a<b:
#         parent[b]=a
#     if b<a:
#         parnet[a]=b
# --------------------------------------
# def is_prime_number(x):
#     for i in range(2,x):
#         if x%i == 0:
#             return False
#     return True
# -------------------------------------
# y=[i for i in range(2,1001)]
# def is_prime_number(x):
#     for j in x:
#         for i in range(2,int(j**(1/2)+1)):
#             if j%i == 0:
#                 y.remove(j)
#                 break
#     return y
#
# print(len(is_prime_number(y)))
# -------------------------------------
import math
n=100
array=[True for _ in range(n+1)]

for i in range(2,int(n**(1/2)+1)):
    if array[i] == True:
        j=2
        while i*j <= n:
            array[i*j] = False
            j+=1
for i in range(2,n+1):
    if array[i]:
        print(i,end=" ")
