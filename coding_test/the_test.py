
def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    num_one = 0
    num_two = 0
    num_three = 0
    a = 0
    b = 0
    c = 0
    end_fir = 4
    end_sec = 7
    end_thi = 9
    num_answer = len(answers)

    for first_person in answers:
        if first_person == first[num_one]:
            a = a+1
        
        if num_one == end_fir:
            num_one = 0
        else:
            num_one = num_one + 1

    for second_person in answers:
        if second_person == second[num_two]:
            b = b+1
        
        if num_two == end_sec:
            num_two = 0
        else:
            num_two = num_two + 1    

    for third_person in answers:
        if third_person == third[num_three]:
            c = c+1
        
        if num_three == end_thi:
            num_three = 0
        else:
            num_three = num_three + 1    

    total_score = [a,b,c]
    print(a,b,c)

    if a>b and a>c:
        answer=[1]
    elif b>a and b>c:
        answer=[2]
    elif c>a and c>b:
        answer=[3]
    elif a==b and a>c:
        answer=[1,2]
    elif a==c and a>b:
        answer=[1,3]
    elif b==c and b>a:
        answer=[2,3]
    elif a==b==c:
        answer=[1,2,3]
    
    return answer
    
solution(answers)

