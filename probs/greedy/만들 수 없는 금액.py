from collections import deque

N = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
d = deque(data)

res = sum(d)+1
while d:
    cur = d.popleft()

    if cur == 1:
        break 

print(res)