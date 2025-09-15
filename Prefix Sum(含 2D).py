# 1D
prefix = [0]
for x in nums:
    prefix.append(prefix[-1] + x)
# sum of [i, j] = prefix[j+1] - prefix[i]

# 2D
m, n = len(grid), len(grid[0])
pre2d = [[0]*(n+1) for _ in range(m+1)]
for i in range(m):
    for j in range(n):
        pre2d[i+1][j+1] = grid[i][j] + pre2d[i][j+1] + pre2d[i+1][j] - pre2d[i][j]
# sum of submatrix [(r1,c1),(r2,c2)]
# = pre2d[r2+1][c2+1]-pre2d[r1][c2+1]-pre2d[r2+1][c1]+pre2d[r1][c1]
