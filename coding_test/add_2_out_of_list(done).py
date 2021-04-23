
numbers=[5,0,2,7]
def solution(numbers):
    answer=[]
    for setnum in numbers:
        first = numbers.index(setnum)
        start = first + 1
        restnum = numbers[start:]

        for rest in restnum:
            result = setnum + rest
            if result not in answer:
                answer.append(result)
    answer = sorted(answer)
    print(answer)

solution(numbers)

## set 함수 사용하기
## set()으로 중복된 list를 없앨 수 있다.