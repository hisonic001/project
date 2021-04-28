from math import ceil

prog = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
done_day_list = []
count_con = 0
count = 0
count_list = []

for i in range(len(speeds)):
    done_day = (100 - prog[i]) / speeds[i]
    done_day_list.append(ceil(done_day))
print(done_day_list)
print(list(range(len(done_day_list))))
print(len(done_day_list) - 1)
done_con = 0
for i in range(len(done_day_list)):
    count_con += 1
    if i == 0:
        done_con = done_day_list[i]
        continue
    elif done_con < done_day_list[i]:
        count = count_con - 1
        count_list.append(count)
        done_con = done_day_list[i]
        count_con = 1
        if i == len(done_day_list) - 1:
            count = count_con
            print(f"마지막 count = {count}")
            count_list.append(count)
            break
    elif i == len(done_day_list) - 1:
        count = count_con
        print(f"마지막 count = {count}")
        count_list.append(count)
        break

print(count_list)
