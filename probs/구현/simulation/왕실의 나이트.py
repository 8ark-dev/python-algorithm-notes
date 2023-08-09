#map 8 x 8
night = input()
cx = int(ord(night[0])) - 97 #a 
cy = int(night[1]) - 1

dx = [-1,1, 2,2, 1, -1, -2, -2]
dy = [2,2,1,-1,-2,-2,-1,1]

res=0
for i in range(8):
    nx = cx + dx[i]
    ny = cy + dy[i]

    if nx < 0 or nx > 7 or ny < 0 or ny > 7:
        continue

    res += 1
print(res)