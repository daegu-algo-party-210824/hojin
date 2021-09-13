# 답안지

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):

        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]

        if j == i:
            up = 0
        else:
            up = dp[i-1][j]

        dp[i][j] = dp[i][j] + max(up, up_left)

print(max(dp[n-1]))


# n = int(input())
# m = []
# for i in range(n):
#     m.append(list(map(int, input().split())))

# dp = []

# for i in range(n, 1, -1):
#     tmp = []
#     for j in range(len(m) - 1):
#         tmp.append(max(m[i][j] + m[n - 1][j], m[i][j + 1] + m[n-1][j]))
#     dp.append(tmp)
