
N = int(input())
data = list(map(int, input().split()))

data.sort()

target = 1

for d in data:
    if target  < d:
        break
    target += d
print(target)