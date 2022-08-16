people_num = int(input())
withdrawal_time = list(map(int, input().split()))

withdrawal_time.sort()

tmp_list = []
tmp_sum = 0
min_sum = 0

for i in range(0, len(withdrawal_time)):    
    tmp_sum += withdrawal_time[i]   
    tmp_list.append(tmp_sum)
    
for i in range(0, len(tmp_list)):
    min_sum += tmp_list[i]
    
print(min_sum)