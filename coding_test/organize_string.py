strings = ["abce", "abcd", "cdx"]
n = 2
dic = {}
num_list = []
answer = []
string = strings.sort()
mid = [strings[i][n] for i in range(len(strings))]
for count, value in enumerate(mid):
    dic[count] = value
dic = sorted(dic.items(), key=lambda item: item[1])
for i in range(len(strings)):
    num_list.append(dic[i][0])
for i in num_list:
    answer.append(strings[i])

# using lambda
print(sorted(strings, key=lambda x: x[n]))
