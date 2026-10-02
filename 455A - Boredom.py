import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    a = [int(x) for x in data[1:1+n]]
    
    if not a:
        print(0)
        return
        
    max_val = max(a)
    count = [0] * (max_val + 1)
    
    for x in a:
        count[x] += 1
        
    dp = [0] * (max_val + 1)
    dp[1] = count[1] * 1
    
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + count[i] * i)
        
    print(dp[max_val])

if __name__ == '__main__':
    solve()
