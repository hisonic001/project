# import random
# # array=["123","456","789"]
# array=[]
# num = str(random.randrange(1,10000))
# for i in range(10):
#     while num in array or num[0] ==0:
#         num = str(random.randrange(1,1000))
#     array.append(num)
# # print(joined,"".join(set(joined)))
array = ["119", "22197674223", "11955244218"]

array.sort()
print(array)

for i in range(len(array)-1):
    if array[i] == array[i+1][:len(array[i])]
        return False
        break
    return True
# def solution(array):
#     for i in array:
#         t = len(i)
#         for y in range(1,t):
#             for x in range(len(array)):
#                 rest = [i for i in range(len(array))]
#                 rest.remove(x)
#                 for i in rest:
#                     box = array[x][-y:]
#                     print(box, array[i][:y])
#                     if box > array[i][:y]:
#                         continue
#                     if box == array[i][:y]:
#                         return False
#         return True
# print(solution(array))
