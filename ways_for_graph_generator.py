arr_a = []
arr_b = []
import random
size = int(input())
for a in range(size):
    arr_a = []
    for b in range(size):
        if a == b:
            arr_a.append(1e8)
        else:
            arr_a.append(0)
    arr_b.append(arr_a)
for x in range(size):
    for y in range(size):
        if arr_b[x][y] == 0:
            rand = random.randint(1,1e3)
            arr_b[x][y] = rand
            arr_b[y][x] = rand
for u in range(len(arr_b)):
    print(arr_b[u])
    
            
