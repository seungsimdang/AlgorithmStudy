def length(n):
    if(n==1 or n==2 or n==3):
        return 1
    
    spiral = [0 for _ in range(0,n+1)]    
    
    spiral[1] = 1
    spiral[2] = 1
    spiral[3] = 1
    
    for i in range(4, n+1):
        spiral[i] = spiral[i-3] + spiral[i-2]
        
    return spiral[n]

t = int(input())

input_arr = [0 for _ in range(0,t)]

for i in range(0,t):
    input_arr[i] = int(input())
    
for i in range(0,t):
    print(length(input_arr[i]))