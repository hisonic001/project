from itertools import permutations, combinations, product, combinations_with_replacement
from collections import Counter
from math import gcd, factorial, pi

data = ["a", "b", "c"]

result = list(permutations(data, 2))
result2 = list(combinations(data, 3))

print(f"1{result} \n\n2{result2}\n\n")

result3 = list(product(data, repeat=2))
result4 = list(combinations_with_replacement(data, 2))

print(f"3{result3} \n\n4{result4}\n\n")


# 내부 원소 몇개 있는지 찾기
# 딕셔너리로 변환 가능
counter = Counter(result3)
print(counter["a", "a"])
print(dict(Counter(result4)), "\n\n")

# 최대 공약수 최소 공배수 찾기
print((lambda a, b: a * b // gcd(a, b))(12, 35))
