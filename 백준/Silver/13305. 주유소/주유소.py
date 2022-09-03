city_num = int(input())
road_len = list(map(int, input().split()))
cost = list(map(int, input().split(' ')))

total_cost = 0
flag = cost[0]

for i in range(0, city_num-1):
    if(flag > cost[i]):
        flag = cost[i]
    total_cost += flag * road_len[i]
        
print(total_cost)
