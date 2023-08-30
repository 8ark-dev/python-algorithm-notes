from collections import deque

s = deque(input())

zero_cnt = 0
one_cnt = 0

cur = s.popleft()

#시작
if cur == '0':
    one_cnt += 1
else:
    zero_cnt += 1

#메인
while s:
    prev = cur
    cur = s.popleft()
    
    print(prev, cur)

    if prev == '0' and cur == '1':
        one_cnt += 1
    elif prev == '1' and cur == '0':
        zero_cnt += 1

#마지막
if prev != cur:
    if cur == '0':
        zero_cnt += 1
    else:
        one_cnt += 1

print((zero_cnt, one_cnt))