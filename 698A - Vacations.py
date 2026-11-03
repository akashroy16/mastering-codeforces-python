import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]
    
    # dp[0]: rest, dp[1]: contest, dp[2]: gym
    dp = [0, 0, 0]
    for x in a:
        next_dp = [0, 0, 0]
        # rest can follow any state
        next_dp[0] = max(dp[0], dp[1], dp[2])
        # contest
        if x == 1 or x == 3:
            next_dp[1] = 1 + max(dp[0], dp[2])
        else:
            next_dp[1] = -float('inf')
        # gym
        if x == 2 or x == 3:
            next_dp[2] = 1 + max(dp[0], dp[1])
        else:
            next_dp[2] = -float('inf')
        dp = next_dp
    print(n - max(dp))

if __name__ == '__main__':
    solve()
