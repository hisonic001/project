from sys import getsizeof #range 용량비교
from typing import TypeVar #generic programing
from dataclasses import dataclass #dataclass(구조체)

# generic programing -> 클래스 내부의 데이터 타입을 외부에서 지정, 데이터 타입에 따라서 다른 방식으로 작동되는 프로그램
# def are_equal(a,b):
#     return a==b
# print(are_equal(10,10.0)) // == True

# T=TypeVar('T')
# U=TypeVar('U')

# def are_equal(a:T,b:U) -> bool:
# # //type hint a는 T타입(datatype), b는 U라는 datatype 지정 return은 bool로 한다고 알려줌
#     return a==b
# print(are_equal(10,10.0))

# from functools import singledispatch
# @singledispatch
# def fun(x):
#     print("This is default behavior:", x)
# @fun.register(int)
# ## x가 정수타입인 경우에는 fun은 아래 코드를 실행하게된다.
# def _(x):
#     print("I like Integer:", x)
# @fun.register(str)
# def _(x):
#     print("string is strong:", x.upper())
# @fun.register(float)
# def _(x):
#     print("floating number is beautifule:", x/2)
# @fun.register(bool)
# def _(x):
#     print("This is bool:", x)
# fun(range(1,3))

# Class(구조체)
# @dataclass
# class Product:
#     weight:int=None # datatype = default value
#     price:float=None
#     def total_price(self):
#         return self.weight*self.price

# apple=Product()
# apple.weight=20
# apple.price=40
# print(apple)
# print(apple.total_price())


# map,lambda (list Comprehension)
# print(list(map(lambda x:x+110,range(1,4))))
# #list accomplihension
# print([i*2 for i in range(1,11) if i%2==1])


# #dictionary complrehension
# original={'app':'salad','main':'stake','desert':'ice_cream'}
# # a={}
# # for key, value in original.items():
# #     a[key]=value
# a = {key:value for key, value in original.items()}
# print(a)


#generator
# def get_natural_number():
#     n=0
#     while True:
#         n+=1
#         yield True #yield n #yield stirng #yield False
# num=get_natural_number()
# for _ in range(50):
#     print(next(num))


# #range 함수
# a = range(10000)
# b = [i for i in range(10000)]
# print(len(a),len(b))
# print(getsizeof(a),getsizeof(b))


#enumerate
# a=['a1','b2','c3']
# # i = 0
# # for v in a:
# #     print(i,v)
# #     i+=1
# for i,j in enumerate(a):
#     print(i,j) #(0,a1)(1,b2)(3,c3)

# //나누기(int) 내림연산, /나누기(float), %나머지, divmod(5,3) 몫,나머지 동시
# print(divmod(10,7))
#->(1,3)
# print(type(10/7))
# ->float
# print(type(10//7))
# ->int
