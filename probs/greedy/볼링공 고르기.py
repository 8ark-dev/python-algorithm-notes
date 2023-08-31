# 볼링공 무게 오름차순으로 정렬하기

N, M = map(int, input().split())
balls = list(map(int, input().split()))

balls.sort()

res = 0

cnt = [] # 각 무게별 공의 개수

for i in range(1,M+1):
    cnt.append( balls.count(i) )

#첫 번째 수를 1부터 M까지 증가시키면서 반대편 개수 세기
for i in range(1, M):
    res += cnt[i-1] * sum(cnt[i:])


print( res ) #순서 바뀌는 것 고려