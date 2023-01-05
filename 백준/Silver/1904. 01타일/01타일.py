n = int(input())

def count(n):
    tmp = [0 for _ in range(n+1)]
    
    if n==1:        
        return 1
    if n==2:        
        return 2    
    tmp[1] = 1
    tmp[2] = 2
    for i in range (3,n+1):
        # 수시로 나머지 연산을 해주어야 메모리 초과가 발생하지 않음
        # (값이 int 범위를 초과하기 때문)
        tmp[i] = (tmp[i-1]+tmp[i-2])%15746 
    return tmp[n]

print(count(n))