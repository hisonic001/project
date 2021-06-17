# import time
# #함수의 실행 시간을 쟤는 함수 @로 함수이전에 데코레이터로 정의가능
# def logging_time(original_fn):
#     def wrapper_fn(*args, **kwargs):
#         start_time = time.time()
#         result = original_fn(*args, **kwargs)
#         end_time = time.time()
#         print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time-start_time))
#         return result
#     return wrapper_fn

numbers=[1,24,223,200,20,2220,3,30,34,5,9,409,405,4,4010]

# def find_bigger_num(num_list):
#     big_num_list=[]
#     for index,num in enumerate(num_list):
#         print(num,type(num), index,type(index))
#         while index<len(num_list)-1:
#             if num == num[index+1]:
#                 print('hjoo')

#             # print(big_num_list)
#     return(big_num_list)

# @logging_time
# def find_big_num(numbers):
#     numbers = sorted(map(str,numbers),key=lambda x:(x[0],len(x)),reverse=True)
#     count=9
#     greatest_num_list=[]
#     while count>0:
#         num_list=[i for i in numbers if i[0] == f'{count}']
#         count-=1
#         greatest_num_list += find_bigger_num(num_list[::-1])
#     return greatest_num_list
#         # print(num_list[::-1])
#     # for  in numbers:
#     #     find_bigger_num(i)


# print(find_big_num(numbers))

def solution(numbers):
    numbers = list(map(str, numbers))
    def lam(x):
        return x*5
    for i in numbers:
        print(lam(i))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))
print(solution(numbers))