n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0   
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = -10
for row in a:
    print(' '.join([str(elem) for elem in row]))