# 2
x,y = input("enter vlaues: ").split(',')
x=int(x)
y=int(y)
mat = [[0 for col in range(y)] for row in range(x)]
for row in range(x):
    for col in range(y):
        mat[row][col] = row*col
print(mat)