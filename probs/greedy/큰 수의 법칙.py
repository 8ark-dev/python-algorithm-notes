N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort() # 2 4 4 5 6

res = 0

#print(nums)
while M>0:
    if K>=M:
        res += nums[-1] * K
        M-=K
        nums.pop()
    else:
        res += nums[-1] * K
        M = 0
        break

print(res)