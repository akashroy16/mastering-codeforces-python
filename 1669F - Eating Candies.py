import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        w = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        left = 0
        right = n - 1
        sum_l = w[0]
        sum_r = w[n - 1]
        max_candies = 0
        
        while left < right:
            if sum_l == sum_r:
                max_candies = max(max_candies, (left + 1) + (n - right))
                left += 1
                sum_l += w[left]
            elif sum_l < sum_r:
                left += 1
                sum_l += w[left]
            else:
                right -= 1
                sum_r += w[right]
        out.append(str(max_candies))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
