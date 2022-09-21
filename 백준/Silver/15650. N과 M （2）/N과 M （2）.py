def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(start, n+1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i) 
        start += 1
        dfs(start)
        arr.pop()
        visited[i] = False


n, m = map(int, input().split())
arr = []
visited = [False for _ in range(n+1)]

dfs(1)