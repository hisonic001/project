array=[5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array,start,end):
#     if start >= end:
#         return
#     pivot = start
#     left = start+1
#     right = end
#     while(left<=right):
#         while(left<=end and array[left] <= array[pivot]):
#             left+=1
#         while(right>start and array[right]>= array[pivot]):
#             right-=1
#         if(left>right):
#             array[right],array[pivot]=array[pivot],array[right]
#         else:
#             array[right],array[left]=array[left],array[right]
#     quick_sort(array,start,right-1)
#     quick_sort(array,right+1,end)
# quick_sort(array,0,len(array)-1)
# print(array)
#
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     pivot = array[0]
#     tail = array[1:]
#
#     left_side = [x for x in tail if x<=pivot]
#     right_side = [x for x in tail if x>pivot]
#
#     return quick_sort(left_side)+[pivot]+quick_sort(right_side)
# print(quick_sort(array))

# def quick_sort(array):
#     count=[0]*(max(array)+1)
#     for i in range(len(array)):
#         count[array[i]] +=1
#     for i in range(len(count)):
#         for j in range(count[i]):
#             print(i, end=' ')
# quick_sort(array)

n,k = 5,3
a = [1,2,5,4,3]
b = [5,5,6,6,5]

a=sorted(a)
b=sorted(b,reverse=True)
for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:break
print(sum(a))
