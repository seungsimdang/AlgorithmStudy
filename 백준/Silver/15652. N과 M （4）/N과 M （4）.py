def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(start, n+1):
        visited[i] = True
        arr.append(i) 
        dfs(i)
        arr.pop()
        visited[i] = False


n, m = map(int, input().split())
arr = []
visited = [False for _ in range(n+1)]

dfs(1)