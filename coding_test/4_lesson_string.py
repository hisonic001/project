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

# # **펠린드롬 찾기 : 앞뒤가 똑같은 단어 ex)기러기, 소주 만명만 주소

# 1. 리스트만으로 풀이
# @logging_time
# def isPelindromeA(s:str) -> bool:
#     letters = []
#     for char in s:
#         if char.isalnum():
#             letters.append(char.lower())
    
#     while len(letters)>1:
#         if letters.pop(0) != letters.pop():
#             return False
#     return True


# 2. deck 자료형을 통해 풀이
# from collections import deque
# from typing import Deque
# @logging_time
# def isPelindromeB(s:str) -> bool:
#     letters:Deque = deque() #덱 자료형 선언
#     for char in s:
#         if char.isalnum():
#            letters.append(char.lower())
#     while len(letters)>1:
#         if letters.popleft() != letters.pop():
#             return False
#     return True

# 3.문자 슬라이싱을 통한 풀이
# import re
# @logging_time
# def isPelindromeC(s:str) -> bool:
#     #정규식으로 불필요한 문자제거
#     # re.sub(pattern,치환할문자,치환할문자열)
#     # 정규식의 pattern 표시할때 []->사이의 문자들과 매치를 의미
#     # -(하이픈)은 A-Z a-z와 같이 from a to z를 의미
#     # [] 안에 ^를 사용시 not(반대)의 의미를 가진다.
#     # /d == [0-9], /D == [^0-9], /s == [공백문자]
#     # /w ==[a-zA-Z0-9] 대문자는 반대(^)
#     s=re.sub('/W','',s)
#     s=s.lower()
#     return s == s[::-1] #슬라이싱, 역순으로 뒤집기

# a='A man, a plan, a cameo, Bird, Mocha, Prowel, a rave, Uganda, Wait, a lobola, Argo, Goto, Koser, Ihab, Udall, a revocation, Ebarta, Muscat, eyes, Rehm, a cession, Udella, E-boat, OAS, a mirage, IPBM, a caress, Etam, FCA, a mica, Ojai, Lebowa, Yaeger, a barge, Rab, Alsatian, a mod, Adv, a rps, Ileane, Valeta, Grenada, Hetty, Fayme, REME, HCM, Tsan, Owena, Tamar, Yompur, Isa, Nil, Lorrin, Riksdag, Mona, Ronn, O’Conner, Kirk, an okay, Nafl, Lira, Robi, Rame, FIFA, a need, Rodi, Muharram, Ober, a coma, carri, Hwang, Taos, Salado, Olfe, Camag, Kdar, a hdkf, Jemina, Nadler, Ehud, Rutan, a baster, Ebn, aedegi, a gals, Ira, Tepper, a minim, a gowd, Ulda, Ogawa, TSgt, Callida, Rodl, Ewart, seraphs, Ain, Newgate, Vaden, navettes, Sabah, Swat, Luci, Pam, Arda, pools, a boar, Akira, Gally, CSC, Avalon, a tuba, AAM, Artima, AFB, Selah, wellies, Ronald, BArch, nullos, Uni, an aet, Nadabus, Tyree, Poop, Sennar, CAB, a nanny, Let, Efahan, Dasya, Moon, Ikaria, Nam, Lamar, Egor, Rover, Tanana, Loki, MIP, PharD, endia, rates, Punan, Eba, Alva, Paine, BEF, Fagan, nugae, taws, Una, Woll, a tab, CSE, Kamerad, YCL, a melt, Diehl, Lewellen, Sacci, Reggi, RFA, BSA, naoi, Kuyp, Oceanic, Sipple, Yalu, Kosey, nota, talers, Frida, a wab, Musset, Aoede, Erick, a reign, Attica, Marge, Leta, Mat, Naboth, Saphra, Gila, Arany, Costa, Fasta, Mabel, Udine, Derte, Medill, Erotes, RuPaul, Uzzi, Waler, Omak, a kaif, Freed, a doc, a marga, Nilla, Dole, USPO, Ogata, tubas, somata, Dash, Danika, Salida, Fiji, Emili, Kazak, Oder, CAC, Ilocanos, Nudd, Uda'
# a=a*500
# print(isPelindromeA(a))
# print(isPelindromeB(a))
# print(isPelindromeC(a))

#----------------------------------------------------------
# 문자열 뒤집기
# 1.투포인터를 사용한 방법
# from typing import List
# char_list=['h','e','l','l','o']
# char_list2=['H','a','n','n','a','h']
# def reverse(self, s=List(str)) -> None:
#     left,right=0,len(s)-1
#     while left<right:
#         s[left],s[right]=s[right],s[left]
#         left+=1
#         right-=1

# 2. 파이썬다운 방법
# def reverse(self,s=List(str)) ->None:
#     s.reverse() #또는 s = s[::-1]로도 풀이 가능
# ---------------------------------------------------------------------------------
# 로그 파일 재정렬
# 우선 문자로그가 숫자로그 보다 우선, 문자로그 중에서 재정렬, 문자로그가 같다면 식별자로 정렬
# from operator import itemgetter   #operator.itemgetter는 itemgetter(x)로 활용하면 sort의 key값에서 몇번쨰 인자로 정렬할지 정할 수 있다.
# logs = ['dig1 9 1 5 1','let1 art can','dig2 3 6','let2 own kit dig','let3 art zero']
# letters,digits=[],[]
# for log in logs:
#     if log.split()[1].isdigit():
#         digits.append(log)
#     else:
#         letters.append(log)
# letters.sort(key=lambda x:(x.split()[1:],x.split()[0]))   #lambda를 통해서 함수를 따로 지정하지 않고 한줄로 처리
# print(letters+digits)
# # ------------------------------------------------------------------------------------------
# 가장 흔한 단어
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분x 구두점 등 무시
# from re import sub
# from collections import defaultdict,Counter
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
# banned = ["hit"]
# words=[i for i in sub('[\W]',' ',paragraph).lower().split() if i not in banned]
# #Counter().most_common()을 통해서 가장 많은 빈도의 단어를 추출
# print(Counter(words).most_common(1))

# ------------------------------------------------------------------------------------------------
# group_anagrams
#  문자열을 받아 애너그램 단위로 그룹핑
# import collections
# words=['eat','tea','tan','ate','nat','bat']
# #default 값으로 리스트를 가지는 딕션너리 생성
# anagram = collections.defaultdict(list)
# for word in words:
#     #anagram[aet].append(eat,tea,ate)
#     #aet의 아나그램을 가지는 딕션너리 리스트에 원래 string인 eat,tea,ate를 append함
#     anagram[''.join(sorted(word))].append(word)
# print(anagram)

# ---------------------------------------------------------------------------------------------------
# 여러가지 정렬방법
a = [2,5,1,2,3,6]
print(sorted(a)) # -> [1,2,2,3,5,6]
b='eoaiwbjsck'
print(''.join(sorted(b))) #-> 'abceijkosw'
c = ['ccc','bb','da','aaaa','f']
print(c.sort()) #--> None 원래 리스트를 sorting 해줄뿐 새로운 리스트는 만들지 않는다.
print(sorted(c)) #--> ['aaaa', 'bb', 'ccc', 'da','f']
print(sorted(c,key=len)) #함수 key를 통해서 sorting 가능, len은 글자 길이 순으로 정렬 -> ['f', 'bb', 'da', 'ccc', 'aaaa']
d = ['cde','cfc','abc']
print(sorted(d,key=lambda x:(x[0],x[-1]))) #문자열의 첫번째 순으로 정렬 후 마지막 문자로 재정렬 -> ['abc', 'cfc', 'cde']
# ------------------------------------------------------------------------------------------------------
# 가장 긴 팰린드롬 부분 문자열 출력하기

class solution:
    def find_logest_pelindrome(self,s:str)->str:
        def expand(left:int,right:int)->str:
            while left>=0 and right<= len(s) and s[left]==s[right-1]:
                left-=1
                right+=1
            return s[left+1:right-1]

        if len(s)<2 or s==s[::-1]:
            return s

        result =''
        for i in range(len(s)-1):
            result = max(result,expand(i,i+1),expand(i,i+2),key=len)
        return result

find=solution()
answer=find.find_logest_pelindrome('123454321')
print(answer)