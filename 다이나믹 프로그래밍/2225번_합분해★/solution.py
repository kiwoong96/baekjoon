N, K = map(int,input().split())

dp = [[0 for i in range(201)] for _ in range(201)]
for i in range(1,N+1):
    dp[i][1] = 1
for j in range(1,K+1):
    dp[1][j] = j
for i in range(2,N+1):
    for j in range(2,K+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1] )% 1000000000

"""for i in range(10):
    for j in range(10):
        print(dp[i][j], end= ' ')
    print()"""


print(dp[N][K])