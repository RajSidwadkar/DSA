def isLucky(n):
    return all(d in '47' for d in str(n))
def LuckyPath(grid):
    row = len(grid)
    col = len(grid[0])

    dp =[[0]* col for _ in range(row)]

    dp[0][0] = 1 if isLucky(grid[0][0]) else 0

    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                continue

            luckyval = 1 if isLucky(grid[i][j]) else 0

            above = dp[i-1][j] if i > 0 else float('-inf')
            left = dp[i][j-1] if j > 0 else float('-inf')

            dp[i][j] = max(above, left) + luckyval

    return dp[row-1][col -1]

print(LuckyPath([[47, 12, 34],
                 [11, 74, 23],  
                 [44, 56, 77]]))
                
