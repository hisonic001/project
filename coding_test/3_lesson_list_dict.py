# List
# a = [1,2,3]
#  삽입,추가
# a.append(4)
# print(a)
# a.insert(1,1.5)
# print(a)
# try:  #예외 발생
    # print(a[5])
# except:     #예외 처리 방법
    # print("list is not available")
#삭제
# del a[] # --> (x)번째 배열의 자료 삭제
# a.remove()  #--> (x) 값이 저장된 배열 삭제
#슬라이싱이 매우 유용 a[1:2] a[:2] a[1:2:2]..


#Dictionary
# a[key]  #value 값 확인
# a[key]=Value #value 값 할당
# key in a  #key 유무 확인
# del a['key'] del로 키값을 정해 dictionary 삭제 가능
# 대부분이 O(1)의 시간복잡도인 우수한 자료형

# a={'key1':'value1','key2':'value2'}
# print(a)
# a['key3']='value3'
# print(a)
# print(a['key1'])
# print('key4' in a)
# try:
#     print(a['key5'])
# except:
#     print("존재하지 않는 키입니다.")

# for key,value in a.items():  #-> items()로 key와 value를 동시에 불러 두 변수에 할당
    # print(f'{key} 값의 value는 {value} 입니다.')

#dictionary modules(collection에 속한 모듈들)
from collections import defaultdict,Counter,OrderedDict
# 1. defaultdict : 존재하지 않는 키를 조회시 에러 대신 default 값을 넣어서 dictionary item 생성
# a=collections.defaultdict(int)
# a['A']=5
# a['B']=4
# print(a) #-> defaultdict(<class 'int'>,{'A': 5, 'B': 4}) 클래스도 defaultdict로 바뀐다.
# a['C']+=1
# print(a) #-> default 값인 0으로 자동 할당되며 +1한 1로 C값이 할당됨.
# 2.Counter
# a = [1,2,3,4,5,6,6,7,7,7,3]
# b = Counter(a) #-> 각 숫자가 몇개씩 있는지 dictionary로 만들어 알려준다
# print(b) #-> Counter({7: 3, 3: 2, 6: 2, 1: 1, 2: 1, 4: 1, 5: 1}) 7:3개 3:2개 6:2개.....
# print(b.most_common(3)) -> collection 중에서 가장 빈도수가 높은 item 3개를 골라 보여준다.
