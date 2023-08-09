N = int(input())

res=0
for i in range(N+1):
    if i == 3 or i == 13:
        res+=3600
    else:
        res+=1575 # 45 * 15 + 15 * 60



