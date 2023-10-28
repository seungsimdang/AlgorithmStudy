import heapq
import sys

n = int(sys.stdin.readline())
maxH, minH, ans = [], [], []

for i in range(n):
    x = int(sys.stdin.readline())

    if (len(maxH) == len(minH)):
        heapq.heappush(maxH, -x)
    else:
        heapq.heappush(minH, x)

    if (maxH and minH and -maxH[0] > minH[0]):
        max_val = heapq.heappop(maxH) * -1
        min_val = heapq.heappop(minH)
        heapq.heappush(maxH, min_val * -1)
        heapq.heappush(minH, max_val)

    ans.append(maxH[0] * -1)

for i in ans:
    print(i)
