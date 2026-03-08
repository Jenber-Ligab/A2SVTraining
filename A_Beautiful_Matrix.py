matrix = []
for _ in range(5):
    x = list(map(int, input().split()))
    matrix.append(x)
#print(matrix)
target = [2,2]
current_pos = []
for i,row in enumerate(matrix):
    if 1 in row:
        current_pos = [i, row.index(1)]
        break
        #print(i+1, row.index(1) + 1)
print(abs(current_pos[0] - target[0]) + abs(current_pos[1] - target[1])) 