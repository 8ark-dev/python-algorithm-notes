from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

q = deque()
q.append((0,0,1))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(): 
    while q:
        x,y,cnt = q.popleft()
        graph[x][y] = -1 #방문처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == N-1 and ny == M-1 :
                return cnt + 1

            if nx <= -1 or nx > N-1 or ny <= -1 or ny > M-1:
                continue

            if graph[nx][ny] == 1:
                q.append((nx,ny,cnt+1))
    
print(bfs())

#실수한 점
# bfs를 재귀로 했는데 return cnt+1로 한 점
