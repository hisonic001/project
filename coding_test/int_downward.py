n = 118382
sorted_num = sorted(str(n), reverse=True)
print(sorted_num)
new_num = list(map(int, sorted_num))
print(int("".join(sorted_num)))

# join은 list를 다시 합쳐주는 함수
