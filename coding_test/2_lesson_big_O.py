# 빅오(O)
#점근접 실행시간을 표기
# 1. O(1) -> O(log n) -> O(n) -> O(n log n) -> O(n**2) -> O(2**n)
# 순서대로 시간복잡도 상승 대체로 n ~ n log n 정도면 적정 수준

# 최선 Ω, 최악 O, 평균의 경우 θ
# 보통은 빅오(O) 상한으로 표기

# 분할상환분석(amortized analysis) : 최악의 경우를 여러번에 걸쳐 골고루 나눠주는 형태로 시간복잡도를 계산
# 병렬회로 : 알고리즘의 병렬화로 실행속도 상승 GPU의 병렬코어들을 사용하여 동시에 여려 연산을 처리


# Datatype(자료형)
# 1. 숫자
# -정수형 : int(정수형), bool(불리언) 불리언 또한 1은 True, 0은 False로 숫자형 데이터 타입의 하위로 들어간다.
# print(True == 1) --> True
# print(False == 0) --> True
# -실수형 : float

# 2. Mapping
# -딕셔너리: {1:'a',2:'b',3:'c'}

# 3.집합
# - set(), {1,2,3,4,5} : 집합자료형으로 중복된 자료를 가지고 있지 않는다. 어느정도 정렬까지 해줌

# 4. sequence
# -가변식(mutable) 시퀀스 : list[]
# -불변식(immutable) 시퀀스 : str,tuple,bytes
# a = (1,2,3,4,5)
# b = (2,3,4)
# print(id(a),id(b))
# a = (1,2,3,4,5,44)
# print(id(a),id(b))
# a[1] = 3


#is와 ==
is는 id값을 비교
==은 할당된 값을 비교  --> 값이 할당 되지 않은 NoneType(Null값)은 ==으로 비교가 불가하다.bytes

