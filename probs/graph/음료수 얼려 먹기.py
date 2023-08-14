N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))
    
#0인 곳으로 들어가서 dfs 돌고 cnt++ 
def dfs(x,y):
    if x<= -1 or x > N-1 or y <= -1 or y > M-1:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    
    return False

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            cnt += 1
        