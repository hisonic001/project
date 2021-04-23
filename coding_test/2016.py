a = 5
b = 24


def solution(a, b):
    answer = ""
    days = 0
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    dates = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    for month, date in dates.items():
        if month == a:
            break
        days = days + date

    days = days + b
    answer = day[days % 7]

    print(answer)


solution(a, b)