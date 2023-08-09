N = int(input()) #map size
move = list(input().split())

idx = 0 #move index
x, y = 1, 1 #starting point 

while idx < len(move):
    if move[idx] == 'L' and y > 1:
        y -= 1
    elif move[idx] == 'R' and y < N:
        y += 1
    elif move[idx] == 'U' and x > 1:
        x -= 1
    elif move[idx] == 'D' and x < N:
        x += 1
    idx+=1

print(x,y)