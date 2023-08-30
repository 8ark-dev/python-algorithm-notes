from collections import deque
import time 


start = time.time()
#input
N = int(input())
data = list(map(int, input().split()))

#sort
data.sort(reverse=True)
d = deque(data)

res = 0

while d:
    print(d)
    cur = d.popleft()
    res += 1

    for _ in range(cur-1):
        if d:
            d.popleft()

print(res)

end = time.time()

print("시간", end-start) #입력을 미리 해놔야 로직 시간만 잴 수 있음.