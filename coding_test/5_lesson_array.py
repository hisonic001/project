#addtion of two numbers
# 덧셈하여 타겟을 만들수 있는 두 숫자 인덱스를 리턴하기
# 1.in을 이용한 탐색
# num, target=[2,7,11,15],9
# def addition(num,target):
#     for n,i in enumerate(num): #숫자와 index를 동시에 선언
#         if target-i in num[n+1:]: #타겟 숫자에서 뺀 수가 리스트에 있는지 확인 [n+1:]을 통해서 중복하여 찾지 않게 해줌
#             return n,num[n+1:].index(target-i)+(n+1) #현 숫자의 index와 타겟 숫자의 인덱스를 확인해 출력

# print(addition(num,target))

# 2. 첫번째 수를 뺀 결과 키 조회
num, target=[2,7,11,15],9
def addition(num,target):
    nums_map={}
    for n, i in enumerate(num):
        nums_map[i]=n
        print(nums_map)
    for n, i in enumerate(num):
        if target-i in nums_map and i != nums_map[target-i]:
            return num.index(i),nums_map[target-i]

print(addition(num,target))

# 3.조회 구조 개선


