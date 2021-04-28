# # 재귀함수 내용이나 프로세스를 무한으로 반복, 종료조건을 사용하는 것이 중요.
# def recursive_function(i):
#     if i == 100:
#         return
#     print(f"{i}번째 재귀함수에서 {i+1} 재귀함수를 호출합니다.")
#     recursive_function(i + 1)
#     print(f"{i}번째 재귀함수를 종료합니다.")


# recursive_function(1)

# -------------------------------------------------------
# 팩토리얼 구현
# from math import factorial

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result


# def factorial_recursive(n):
#     if n <= 1:
#         return 1
#     return n * factorial_recursive(n - 1)


# print(factorial(15))
# print(factorial_recursive(15))
# -------------------------------------------------------------------
# 유클리드 호제법 (최대공약수 계산)
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))
