max_num = int(input().rstrip())
timetable = [list(map(int, input().rstrip().split())) for _ in range(max_num)]

timetable.sort(key = lambda x:(x[1], x[0])) 

count = 0
latest = -1

for i in timetable:
    if latest <= i[0]:
        count+=1
        latest = i[1]

print(count)