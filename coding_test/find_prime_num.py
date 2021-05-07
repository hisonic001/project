from itertools import permutations

numbers="011"
num_list=[]
numbers=sorted(list(map(int,numbers)))
def find_prime_num(num):
    for i in range(2,int(num**1/2)+1):
        if num%i == 0:
            return True
    return False
def solution(number):
    numbers=sorted(list(map(int,number)))
    numlist=[]
    count = 0
    for j in range(1, len(numbers)+1):
        for i in permutations(numbers,j):
            num = int("".join(list(map(str,i))))
            if num == 0 or num == 1:
                continue
            num_list.append(num)
    num_list=set(num_list)
    for i in num_list:
        if find_prime_num(i)==False:
            count+=1
    print(count)
        # if find_prime_num() == True:
        #     count+=1
