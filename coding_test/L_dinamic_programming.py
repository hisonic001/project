# memorization  활용 // 피보나치 수열
# d=[0]*100
# def fibo(x):
#     print('f(' +str(x)+')',end="\n")
#     if x==1 or x==2:
#         return 1
#     if d[x] !=0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
#
# fibo(6)
#
# print(d)
# -------------------------------------------------------------------
# n = 4
# dp = [0]*n
# ware = [1,3,1,5]
# dp[0] = ware[0]
# dp[1] = max(ware[1],ware[0])
#
# for i in range(2,len(ware)):
#     dp[i] = max(dp[i-1],dp[i-2]+ware[i])
#
# print(max(dp))
# ---------------------------------------------------------
#
# x=26
# dp = [0]*30001
#
# for i in range(2,x+1):
#     dp[i] = dp[i-1]+1
#     if i%2 == 0:
#         dp[i] = min(dp[i],dp[i//2]+1)
#     if i%3 == 0:
#         dp[i] = min(dp[i],dp[i//3]+1)
#     if i%5 == 0:
#         dp[i] = min(dp[i],dp[i//5]+1)
# print(dp[x])
# ----------------------------------------------------------------------
# t = 2 #input()
# n,m = 3,4
# array=[[0]*m for _ in range(n)]
# dp=[[0]*m for _ in range(n)]
# opp=[]
# count = 0
# st_num_list=[]
# up=0
# down=0
# left=0
# num_list = '1 3 3 2 2 1 4 1 0 6 4 7'
# num_list = list(map(int,num_list.split(" ")))
# for i in range(n):
#     for j in range(m):
#         array[i][j] = num_list[count]
#         count+=1
# for j in range(m):
#     for i in range(n):
#         if j == 0:
#             dp[i][j] = array[i][j]
#             continue
#         if i-1 >= 0:
#             up = dp[i-1][j-1]
#         if i+1 < n:
#             down = dp[i+1][j-1]
#         left = dp[i][j-1]
#         dp[i][j] = array[i][j]+max(up,down,left)
#
# print(dp)
# print(array)
# -----------------------------------------------------------------
# n=7
# pow = [15,11,4,8,5,2,4]
# df = [0]*len(pow)
# df[0]=0
# for i in range(1,len(pow)-1):
#     print(i,end="")
#     if pow[i]<pow[i+1]:
#         df[i]=df[i-1]+1
#     else : df[i]=df[i-1]
# print(df)
# -----------------------------------
# LIS 증가하는 부분 수열 알고리즘
# 증가하는 형태로 가장 많은 수열이 몇개인지 dp에 넣을 수 있다.
n=int(input())
dp = [1]*n
for i in range(1,n):
    for j in range(0,i):
        if array[i]>array[j]:
            dp[i] = max(dp[i],dp[j]+1)
