N, M = map(int, input().split())
x, y, d = map(int, input().split())

my_map = []

for _ in range(N):
    my_map.append(list(map(int, input().split())))

#북 동 남 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

pt = d #보고있는 방향

res=0

#시작위치
my_map[x][y] = 2
res+=1


end = False

while end == False:
    flag = False
    for i in range(4):
        pt = (pt+3) % 4
        nx = x + dx[pt]
        ny = y + dy[pt]

        if my_map[nx][ny] == 0:
            my_map[nx][ny] = 2
            res+=1
            x = nx
            y = ny
            flag = True
            break
        
    if flag == False:
        nx = x - dx[pt]
        ny = y - dy[pt]
        if my_map[nx][ny] == 1:
            end = True
        else:
            x = nx
            y = ny

print(res)
